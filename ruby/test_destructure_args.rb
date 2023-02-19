def say_hi((one, two), three)
  [one, two, three]
end

say_hi 1, 2 # => [1, nil, 2]

say_hi [1,2,3], 4 # => [1, 2, 4]
