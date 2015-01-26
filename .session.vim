let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <expr> <Nul> jedi#complete_string(0)
inoremap <silent> <S-Tab> =BackwardsSnippet()
inoremap <C-Tab> 	
map! <S-Insert> <MiddleMouse>
map  h
snoremap <silent> 	 i<Right>=TriggerSnippet()
map <NL> j
map  k
map  l
nnoremap <silent>  :CtrlP
snoremap  b<BS>
nnoremap   za  " for toggling folds in vim
snoremap % b<BS>%
snoremap ' b<BS>'
map ;h :Dbg here
map ;b Oimport ipdb; ipdb.set_trace() # BREAKPOINT
map ;w :Dbg watch
map ;d :Dbg down
map ;u :Dbg up
map ;r :Dbg run
map ;t :Dbg out
map ;i :Dbg into
map ;o :Dbg over
vnoremap ;s :sort
map ;l :tabnext
map ;k :tabprevious
vnoremap < <gv  " better indentation
vnoremap > >gv  " better indentation
nmap Q gqap
vmap Q gq
snoremap U b<BS>U
snoremap \ b<BS>\
snoremap ^ b<BS>^
snoremap ` b<BS>`
nmap gx <Plug>NetrwBrowseX
snoremap <Left> bi
snoremap <Right> a
snoremap <BS> b<BS>
snoremap <silent> <S-Tab> i<Right>=BackwardsSnippet()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
map <S-Insert> <MiddleMouse>
inoremap  
inoremap 	 =InsertTabWrapper()
inoremap <silent> <NL> =OmniPopup('j')
inoremap <silent>  =OmniPopup('k')
inoremap <silent> 	 =ShowAvailableSnips()
inoremap " =QuoteDelim('"')
inoremap ' =QuoteDelim("'")
inoremap ( ()i
inoremap ) =ClosePair(')')
inoremap [ []i
inoremap ] =ClosePair(']')
inoremap { {}i
inoremap } =ClosePair('}')
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set autoread
set background=dark
set backspace=2
set cindent
set clipboard=unnamed
set completeopt=longest,menuone
set fileencodings=ucs-bom,utf-8,default,latin1
set guifont=Monospace\ 12
set guioptions=aegit
set helplang=en
set hlsearch
set ignorecase
set incsearch
set laststatus=2
set mouse=a
set pastetoggle=<F2>
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/bundle/ctrlp.vim,~/.vim/bundle/jedi-vim,~/.vim/bundle/pyflakes-vim,~/.vim/bundle/supertab,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim74,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/bundle/jedi-vim/after,~/.vim/after
set shiftround
set shiftwidth=4
set showcmd
set smartcase
set smartindent
set softtabstop=4
set splitbelow
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{CurDir()}%h\ \ \ Line:\ %l/%L%{GitBranch()}
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set noswapfile
set tabstop=4
set termencoding=utf-8
set textwidth=79
set undolevels=700
set wildignore=*.pyc,*_build/*,*/coverage/*
set window=37
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/distributed/Apriori
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +0 apriori.py
args apriori.py
edit apriori.py
set splitbelow splitright
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <expr> <C-Space> jedi#complete_string(0)
noremap <buffer> <silent>  :PyflakesUpdate
nnoremap <buffer> ;r :call jedi#rename()
nnoremap <buffer> ;n :call jedi#usages()
nnoremap <buffer> ;d :call jedi#goto_definitions()
nnoremap <buffer> ;g :call jedi#goto_assignments()
nnoremap <buffer> <silent> K :call jedi#show_documentation()
noremap <buffer> <silent> dw dw:PyflakesUpdate
noremap <buffer> <silent> dd dd:PyflakesUpdate
noremap <buffer> <silent> u u:PyflakesUpdate
inoremap <buffer> <silent> . .=jedi#complete_string(1)
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal balloonexpr=
setlocal nobinary
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal cindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
set colorcolumn=80
setlocal colorcolumn=80
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:XCOMM,n:>,fb:-
setlocal commentstring=#%s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=2
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal foldcolumn=0
set nofoldenable
setlocal nofoldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=indent
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=0
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=
setlocal indentkeys=0{,0},:,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
setlocal nolinebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=jedi#completions
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal smartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=.py
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=8
setlocal tags=
setlocal textwidth=79
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
set nowrap
setlocal nowrap
setlocal wrapmargin=0
let s:l = 159 - ((5 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
159
normal! 010|
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
