" Author: farenjihn <farenjihn@gmail.com>, w0rp <devw0rp@gmail.com>
" Description: Lints java files using javac

let s:classpath_sep = has('unix') ? ':' : ';'

call ale#Set('java_javac_executable', 'javac')
call ale#Set('java_javac_options', '')
call ale#Set('java_javac_classpath', '')

function! ale_linters#java#javac#GetImportPaths(buffer) abort
    let l:pom_path = ale#path#FindNearestFile(a:buffer, 'pom.xml')

    if !empty(l:pom_path) && executable('mvn')
        return ale#path#CdString(fnamemodify(l:pom_path, ':h'))
        \ . 'mvn dependency:build-classpath'
    endif

    let l:classpath_command = ale#gradle#BuildClasspathCommand(a:buffer)
    if !empty(l:classpath_command)
        return l:classpath_command
    endif

    return ''
endfunction

function! s:BuildClassPathOption(buffer, import_paths) abort
    " Filter out lines like [INFO], etc.
    let l:class_paths = filter(a:import_paths[:], 'v:val !~# ''[''')
    call extend(
    \   l:class_paths,
    \   split(ale#Var(a:buffer, 'java_javac_classpath'), s:classpath_sep),
    \)

    return !empty(l:class_paths)
    \   ? '-cp ' . ale#Escape(join(l:class_paths, s:classpath_sep))
    \   : ''
endfunction

function! ale_linters#java#javac#GetExecutable(buffer) abort
    return ale#Var(a:buffer, 'java_javac_executable')
endfunction

function! ale_linters#java#javac#GetCommand(buffer, import_paths) abort
    let l:cp_option = s:BuildClassPathOption(a:buffer, a:import_paths)
    let l:sp_option = ''

    " Find the src directory, for files in this project.
    let l:src_dir = ale#path#FindNearestDirectory(a:buffer, 'src/main/java')
    let l:sp_dirs = []

    if !empty(l:src_dir)
        call add(l:sp_dirs, l:src_dir)

        " Automatically include the jaxb directory too, if it's there.
        let l:jaxb_dir = fnamemodify(l:src_dir, ':h:h')
        \   . (has('win32') ? '\jaxb\' : '/jaxb/')

        if isdirectory(l:jaxb_dir)
            call add(l:sp_dirs, l:jaxb_dir)
        endif

        " Automatically include the test directory, but only for test code.
        if expand('#' . a:buffer . ':p') =~? '\vsrc[/\\]test[/\\]java'
            let l:test_dir = fnamemodify(l:src_dir, ':h:h:h')
            \   . (has('win32') ? '\test\java\' : '/test/java/')

            if isdirectory(l:test_dir)
                call add(l:sp_dirs, l:test_dir)
            endif
        endif
    endif

    if !empty(l:sp_dirs)
        let l:sp_option = '-sourcepath '
        \   . ale#Escape(join(l:sp_dirs, s:classpath_sep))
    endif

    " Create .class files in a temporary directory, which we will delete later.
    let l:class_file_directory = ale#engine#CreateDirectory(a:buffer)
    let l:executable = ale_linters#java#javac#GetExecutable(a:buffer)

    " Always run javac from the directory the file is in, so we can resolve
    " relative paths correctly.
    return ale#path#BufferCdString(a:buffer)
    \ . ale#Escape(l:executable)
    \ . ' -Xlint'
    \ . ' ' . l:cp_option
    \ . ' ' . l:sp_option
    \ . ' -d ' . ale#Escape(l:class_file_directory)
    \ . ' ' . ale#Var(a:buffer, 'java_javac_options')
    \ . ' %t'
endfunction

function! ale_linters#java#javac#Handle(buffer, lines) abort
    " Look for lines like the following.
    "
    " Main.java:13: warning: [deprecation] donaught() in Testclass has been deprecated
    " Main.java:16: error: ';' expected

    let l:directory = expand('#' . a:buffer . ':p:h')
    let l:pattern = '\v^(.*):(\d+): (.+):(.+)$'
    let l:col_pattern = '\v^(\s*\^)$'
    let l:symbol_pattern = '\v^ +symbol: *(class|method) +([^ ]+)'
    let l:output = []

    for l:match in ale#util#GetMatches(a:lines, [l:pattern, l:col_pattern, l:symbol_pattern])
        if empty(l:match[2]) && empty(l:match[3])
            let l:output[-1].col = len(l:match[1])
        elseif empty(l:match[3])
            " Add symbols to 'cannot find symbol' errors.
            if l:output[-1].text is# 'error: cannot find symbol'
                let l:output[-1].text .= ': ' . l:match[2]
            endif
        else
            call add(l:output, {
            \   'filename': ale#path#GetAbsPath(l:directory, l:match[1]),
            \   'lnum': l:match[2] + 0,
            \   'text': l:match[3] . ':' . l:match[4],
            \   'type': l:match[3] is# 'error' ? 'E' : 'W',
            \})
        endif
    endfor

    return l:output
endfunction

call ale#linter#Define('java', {
\   'name': 'javac',
\   'executable_callback': 'ale_linters#java#javac#GetExecutable',
\   'command_chain': [
\       {'callback': 'ale_linters#java#javac#GetImportPaths', 'output_stream': 'stdout'},
\       {'callback': 'ale_linters#java#javac#GetCommand', 'output_stream': 'stderr'},
\   ],
\   'callback': 'ale_linters#java#javac#Handle',
\})
