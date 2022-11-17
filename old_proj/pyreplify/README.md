# pyreplify
### Abandoned

This was an attempt to execute a python script line by line in the python REPL,
so that the value of each line was shown, just like in python interactive mode.
It would speed up prototyping and was especially conceived for mathematical
scripts, so that the result of each side calculation was shown, and printing
things was easier. Vim integration was even attempted by [Diogo Tito](https://github.com/diogotito).

However I realized half way that this was much harder to do than I expexted,
requiring python parsing and semantic analysis, since python is ambiguous
because of semantic whitespace; there was also some trouble with stuff like doc
strings.
