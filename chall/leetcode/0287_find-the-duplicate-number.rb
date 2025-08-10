def find_duplicate(nums)
  # insight: treat the array as a linked list/recursive function for floyd's
  # this works because it has n+1 nodes and values are all <= n
  # in effect, if two nodes have the same value, they'll point to the same 'next'
  t = nums[0]
  h = nums[nums[0]]
  while t != h
    t = nums[t]
    h = nums[nums[h]]
  end

  mu = 0
  t = 0
  while t != h
    t = nums[t]
    h = nums[h]
    mu += 1
  end 

  t
end

