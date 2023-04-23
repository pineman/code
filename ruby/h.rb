def h(binding, *arg)
  h = Hash.new
  arg.each { h[_1] = eval(_1.to_s, binding) }
  h
end

a = 2
b = 3
p(h(binding, :a, :b))

p({a:, b:})
