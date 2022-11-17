" Like the Python REPL but love Vim too much? REPLify your buffers!
function! ToggleREPLify()
    "Toggle the flag (or set it if it doesn't yet exist)...
    let b:REPLified = exists('b:REPLified') ? !b:REPLified : 1

    if b:REPLified
        let w:pyreplify_cursor_pos = getpos('.')
        %!./wrap.py --quiet
    else
        v/^\(>>> \|\.\.\. \)/d      |" Only keep lines starting with >>> or ...
        %s///                       |" Delete the >>> and ... in every line
        call setpos('.', w:pyreplify_cursor_pos)
    endif
endfunction

" Example mapping
nnoremap <silent> <F5> :silent call ToggleREPLify()<CR>
