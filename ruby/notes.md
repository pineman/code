https://ruby-doc.org
https://rubyreferences.github.io/rubychanges/evolution.html
https://pragprog.com/titles/ruby5/programming-ruby-3-2-5th-edition/
https://www.ruby-lang.org/en/documentation/faq/
https://gorails.com
https://exercism.org/tracks/ruby/concepts
https://guilhermesimoes.github.io/blog/installing-gems-per-project-directory

* list all methods of obj and where they're defined:
`obj.methods.collect {|m| "#{m} defined by #{obj.method(m).owner}"}`
more simply: `ls obj` in irb. there's also `show_source obj.method`

