# Elixir notes

## Syntax
https://elixir-lang.org/getting-started/introduction.html
https://elixir-lang.org/crash-course.html
https://elixir-lang.org/getting-started/optional-syntax.html
https://media.pragprog.com/titles/elixir/ElixirCheat.pdf
https://devhints.io/elixir
### Literals
all sigils
number: 31_337, 5e-3
tuple (array): {:ok, 1, 2, 3}
list: [1, 2, 3]
kw list: [{:atom, value}] -> list of 2 elem tuple (atom: value as last arg)
map: %{ key => value, atom: value }

## Phoenix/LiveView
https://filipecabaco.com/post/2022-09-13_realtime_updates_with_liveview

## Linters
https://github.com/hrzndhrn/recode
https://github.com/adobe/elixir-styler
https://github.com/rrrene/credo

## Editors
https://github.com/KronicDeth/intellij-elixir
### For go to definition in vscode elixir-ls
install any elixir version using asdf, then uninstall
`asdf install elixir 1.14.4`
`asdf uninstall elixir`
then follow:
https://elixirforum.com/t/can-i-point-elixir-lsp-to-built-in-module-sources/41564/2
no idea why installing and uninstalling elixir by the plugin is necessary for `elixir path:...` versions to be picked up, but it is

## Repos to learn from
https://github.com/sasa1977/aoc
https://github.com/sasa1977/demo_system
https://github.com/elixirkoans/elixir-koans
https://github.com/devonestes/fast-elixir#combining-lists-with--vs--code
