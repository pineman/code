def a &b
  p yield 2
  binding.irb
end

a { |x| x+2 }
