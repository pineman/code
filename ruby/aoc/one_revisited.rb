a = IO.readlines('one', chomp:true).chunk(&:empty?).map { _2.sum(&:to_i) }.sort
p a[-1]
p a[-3..-1].sum
