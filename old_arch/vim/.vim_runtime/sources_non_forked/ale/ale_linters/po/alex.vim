" Author: Cian Butler https://github.com/butlerx
" Description: alex for PO files

call ale#linter#Define('po', {
\   'name': 'alex',
\   'executable': 'alex',
\   'command': 'alex %s -t',
\   'output_stream': 'stderr',
\   'callback': 'ale#handlers#alex#Handle',
\   'lint_file': 1,
\})
