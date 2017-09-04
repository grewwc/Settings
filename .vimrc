set nocompatible
filetype off
execute pathogen#infect()
syntax on
filetype plugin indent on

let g:go_play_open_browser = 1

set foldmethod=manual



set wildmenu
set showcmd

set hlsearch
set autoindent
set textwidth=120
set t_Co=256
set showmatch
set nohlsearch
set backspace=2
set ruler
set visualbell

set mouse=a
set number

set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set scrolloff=10


colorscheme gruvbox
set background=dark


"""inoremap <C-Space> <C-x><C-o>
inoremap <C-@> <C-x><C-o>

nnoremap <C-z> <Esc>:w<CR>
inoremap <C-z> <Esc>:w<CR>

au BufRead,BufNewFile *.asm set filetype=nasm
