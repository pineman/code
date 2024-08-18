# ruby 3.2
# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, val)
  return 0 if nums.size == 0
  l, r = 0, nums.size - 1
  loop do
    r -= 1 while nums[r] == val && r >= 0
    l += 1 while nums[l] != val && l < nums.size
    break if l > r
    nums[l], nums[r] = nums[r], nums[l]
    r -= 1
  end
  r + 1
end

# Realized afterwards that swapping the non-target values to the beginning
# results in cleaner code vs swapping the target values to the end.
def remove_element(nums, val)
  return 0 if nums.size == 0
  l = 0
  nums.each_with_index do |v, i|
    if v != val
      nums[l], nums[i] = nums[i], nums[l]
      l += 1
    end
  end
  l
end
