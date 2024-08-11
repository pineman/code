# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  r = 0
  (1...nums.size).each { |l|
    if nums[r] != nums[l]
      r += 1
      nums[r], nums[l] = nums[l], nums[r]
    end
  }
  r + 1
end
