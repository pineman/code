p IO.readlines('one', chomp:true).chunk(&:empty?).map { _2.sum(&:to_i) }.max
