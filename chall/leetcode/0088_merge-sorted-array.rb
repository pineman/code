# Ruby 3.2
# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
  e = m+n-1
  m -= 1
  n -= 1
  while e >= 0
  one = m >= 0 ? nums1[m] : (-10e9.to_i - 1)
  two = n >= 0 ? nums2[n] : (-10e9.to_i - 1)
  if one > two
    nums1[e] = one
    m -= 1
  else
    nums1[e] = two
    n -= 1
  end
  e -= 1
  end
end
