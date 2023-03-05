# goal: something like pythons f'{a=}'
def d &b
  yield.map(&:to_s).each { |s|
    print "#{s} = #{eval(s, b.binding)}, "
  }
  puts
end

a = 2
b = 3
d {[:a, :b]}
