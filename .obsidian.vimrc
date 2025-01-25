syntax on

" use spaces instead of tabs
set expandtab

" set 1 tab to 4 spaces
set shiftwidth=4
set tabstop=4


""""" some fixes for shortcommings in obsidian's vim mode """""

" CTRL + R in normal mode does not work for to redo (undo is u)
" is this actually needed?
" nmap <C-r> 

" set CTRL + U and CTRL to go up and down
nmap <C-u> 10gk <CR>
nmap <C-d> 10gj <CR>

" the CTRL + U/D mapping works for Linux and Windows, but for MacOS, the mapping should be to D instead of R.
" The if-statements below might work
" if has('win32')
"     nmap <C-u> 10k <CR>
"     nmap <C-d> 10j <CR>
" elseif has('mac')
"     nmap <D-u> 10k <CR>
"     nmap <D-d> 10j <CR>
" elseif has('unix')
"     nmap <C-u> 10k <CR>
"     nmap <C-d> 10j <CR>
" endif


