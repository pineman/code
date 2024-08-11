# @param {Integer[]} nums
# @return {Integer}
# Whatever I came up with:
# inplace get all uniq numbers together then count them.
# counting once at the start to protect against worst case majority is all bunched up at the end.
# the first part is O(n^2) but could be faster wihout using .index - keeping a pointer to the last next_cur and searching from there on. wont ever be O(n) tho
# def majority_element(nums)
#   return nums[0] if nums.size == 1
#   t = nums.size/2
#   c, cc = nums[0], 1
#   nums[1..].each.with_index { |v, i|
#   if c == v
#     cc += 1
#     return v if cc > t
#   else
#     c, cc = v, 1
#   end
#   }
#   cur_i = 0
#   while cur_i < nums.size - 1
#   nex = cur_i+1
#   cur = nums[cur_i]
#   nex_cur = nums[nex..].index(cur)
#   if nex_cur
#     nex_cur += nex
#     nums[nex], nums[nex_cur] = nums[nex_cur], nums[nex]
#   end
#   cur_i += 1
#   end
#   t = nums.size/2
#   c, cc = nums[0], 1
#   nums[1..].each.with_index { |v, i|
#   if c == v
#     cc += 1
#     return v if cc > t
#   else
#     c, cc = v, 1
#   end
#   }
# end

# Moore voting
def majority_element(nums)
  return nums[0] if nums.size == 1
  t = nums.size/2
  c, cc = nums[0], 1
  nums[1..].each.with_index { |v, i|
  if c == v
    cc += 1
    return v if cc > t
  else
    cc -= 1
    if cc == 0
    c, cc = v, 1
    end
  end
  }
  c
end
