#!/bin/sh
clone() {
  git submodule add -f $1 $2
  cd $2
  git checkout main || git checkout master
  cd -
}
clone git@github.com:pineman/abra.git proj/abra
clone git@github.com:pineman/blackjack.git proj/blackjack
clone git@github.com:pineman/wordmorph.git proj/wordmorph
clone git@github.com:pineman/wordfind.git proj/wordfind
clone git@github.com:hackerschool/ledmatrix.git proj/LEDmatrix
clone git@github.com:hackerschool/r2p.git proj/r2p
clone git@github.com:pineman/psis proj/psis
clone git@github.com:pineman/pineman.github.io.git proj/homepage
clone git@github.com:pineman/services.git proj/services
clone git@gitlab.com:pineman/ju.git proj/ju
clone git@github.com:pineman/abra-go.git proj/abra-go
clone git@github.com:pineman/abra_elixir.git proj/abra_elixir
clone git@github.com:pineman/aoc.git chall/aoc
clone git@github.com:pineman/bolt_invoices.git proj/bolt_invoices
clone https://github.com/github/gitignore git/gitignore
git clone https://github.com/sasa1977/elixir-in-action elixir/elixir-in-action
git clone https://github.com/sasa1977/demo_system elixir/demo_system
git clone https://github.com/dnlserrano/elixir-workshop elixir/elixir-workshop
git clone https://github.com/sasa1977/aoc elixir/aoc
