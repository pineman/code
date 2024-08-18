# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
    h = {}
    nums.each_with_index { |n, i|
        return true if h.key?(n) && i - h[n] <= k
        h[n] = i
    }
    false
end
