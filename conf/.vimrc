" Vundle Setting
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'
Plugin 'The-NERD-tree'
Plugin 'jellybeans.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'ctrlp.vim'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Plugin 'tpope/vim-fugitive'


call vundle#end()
filetype plugin indent on

" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line


" alpa44's setting

" leader key 변경
let mapleader="\<space>"

" Swap 파일 위치변경
set swapfile

" Backup 파일 off
set nobackup

" tab to spaces
set expandtab

" Syntax Highlighting
if has("syntax")
    syntax on
endif

" 자동 인덴트
set autoindent
set cindent " C언어 자동인덴트
set smartindent

" 줄번호
set number

" colorscheme
colorscheme jellybeans

" 인덴트
set tabstop=4
set shiftwidth=4
set softtabstop=4

"  마지막으로 수정된 곳에 커서를 위치함
au BufReadPost * if line("'\"") > 0 && line("l\"") <= line("$") | exe "norm g`\"" | endif

" 검색어 하이라이팅
set hlsearch

" 작업 중인 파일 외부에서 변경됐을 경우 자동으로 불러옴
set autoread

"  붙여넣기 계단현상 없애기
set nopaste

" 일치하는 괄호 하이라이팅
set showmatch

" 파일 인코딩을 한국어로
set fileencoding=korea
set fileencodings=utf8,euckr
set encoding=utf8

" 대소문자 없애기(스마트 적용)
set ignorecase
set smartcase

" 파일 탭 열때 syntax highlighting 적용
" augroup EnableSyntaxHighlighting
"    autocmd! BufWinEnter,WinEnter * nested if exists('syntax_on') && !exists('b:current_syntax') && !empty(&l:filetype) && index(split(&eventignore, ','), 'Syntax') == -1 | syntax enable | endif
"    autocmd! BufRead * if exists('syntax_on') && exists('b:current_syntax') && !empty(&l:filetype) && index(split(&eventignore, ','), 'Syntax') != -1 | unlet! b:current_syntax | endif
"augroup END

" ctrlP
let g:ctrlp_map = '<leader>p'
let g:ctrlp_cmd = 'CtrlP $HOME/workspace'
" 버퍼에서 검색
" nnoremap <c-p>r :CtrlP D:\ICIS_RELEASE\RS<cr>
" nnoremap <c-p>n :CtrlP D:\ICIS_RELEASE\NS<cr>

let g:ctrlp_by_filename = 1 " 파일이름으로 찾기(disable : 0)
let g:ctrlp_regexp = 0      " regexp로 찾기(enable : 1)
let g:ctrlp_working_path_mode = 0
let g:ctrlp_max_files = 0
let g:ctrlp_clear_cache_on_exit = 0
let g:ctrlp_cache_dir = $HOME.'/.cache/ctrlp'
let g:ctrlp_custom_ignore = {
    \'dir':'\Autoext$\|\Dict$\|Misc$\|res$',
    \'file':'\.pyc$\|\.clw$\|\.def$\|\.dsp$\|\.dsw$\|\.ncb$\|\.opt$\|\.PLG$\|\.positions$\|\.rc$\|\.pch\|\.dll$|\.clww$|\.ini$|\.lib$|\.MAK$'
\}



" vim-airline
set laststatus=2
let g:airline_detect_modified = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#fnamemod = ':t'

" Buffer 세팅
" 저장되지 않은 버퍼를 hidden처리
set hidden

nnoremap <c-n> :enew<cr>    "버퍼열기
nnoremap <c-l> :bnext<cr>   "다음버퍼이동
nnoremap <c-h> :bprevious<cr> "이전버퍼이동
nnoremap <leader>bq :bp <bar> bd #<cr> "현재 버퍼를 닫고 이전 버퍼로 이동
nnoremap <leader>bl :ls<cr> " 모든 버퍼와 각 버퍼 상태 출력

" vimrc 편집 단축기
nnoremap <Leader>rc :e $HOME/.vimrc<cr>

" NERDTree세팅
nnoremap <Leader>n :NERDTreeToggle<cr>
nnoremap <Leader>f :NERDTreeFind<cr>

" use system clipboard 
set clipboard=unnamed

" Enter시 자동주석 제거
au FileType * set fo-=c fo-=r fo-=o


" python setting
au BufNewFile,BufRead *.py 
  \ set tabstop=4 |
  \ set softtabstop=4 |
  \ set shiftwidth=4 |
  \ set textwidth=79 |
  \ set expandtab |
  \ set autoindent |
  \ set fileformat=unix |
  \ let python_highlight_all=1

" frontend development setting
au BufNewFile,BufRead *.js, *.html, *.css 
  \ set tabstop=2 
  \ set softtabstop=2 
  \ set shiftwidth=2
