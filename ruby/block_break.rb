def m
  i = 0
  while 1
    i += 1
    yield i
  end
end

m { |i| puts i; break if i >= 5 }
