#!/bin/sh
submodule() {
  git submodule add -f $1 $2
  cd $2
  git checkout main || git checkout master
  git pull
  cd -
}
submodule git@github.com:pineman/abra.git proj/abra
submodule git@github.com:pineman/blackjack.git proj/blackjack
submodule git@github.com:pineman/wordmorph.git proj/wordmorph
submodule git@github.com:pineman/wordfind.git proj/wordfind
submodule git@github.com:hackerschool/ledmatrix.git proj/LEDmatrix
submodule git@github.com:hackerschool/r2p.git proj/r2p
submodule git@github.com:pineman/psis proj/psis
submodule git@github.com:pineman/pineman.github.io.git proj/homepage
submodule git@github.com:pineman/services.git proj/services
submodule git@github.com:pineman/abra-go.git proj/abra-go
submodule git@github.com:pineman/abra_elixir.git proj/abra_elixir
submodule git@github.com:pineman/aoc.git chall/aoc
submodule git@github.com:pineman/bolt_invoices.git proj/bolt_invoices
submodule git@github.com:pineman/su.git proj/su
submodule git@github.com:pineman/fpt.git proj/fpt

submodule https://github.com/github/gitignore git/gitignore
git clone https://github.com/sasa1977/elixir-in-action elixir/elixir-in-action
git clone https://github.com/sasa1977/demo_system elixir/demo_system
git clone https://github.com/dnlserrano/elixir-workshop elixir/elixir-workshop
git clone https://github.com/sasa1977/aoc elixir/sasa-aoc
