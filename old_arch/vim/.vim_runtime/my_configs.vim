"autocmd vimenter * NERDTree
set number
set relativenumber
colorscheme solarized
#colorscheme gruvbox
set nowrap
let g:ale_completion_enabled = 1
set nofoldenable
autocmd FileType * exe "normal zR"
au WinEnter * set nofen
au WinLeave * set nofen
let g:vim_markdown_folding_disabled=1
foldlevel=20
foldlevelstart=20

