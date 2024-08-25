# @param {Integer[]} nums
# @return {String[]}
def summary_ranges(nums)
    return [] if nums.empty?
    ranges = []
    l = r = nums[0]
    nums[1..].each { |i|
        next (r += 1) if r + 1 == i
        ranges << (r == l ? l.to_s : "#{l}->#{r}")
        r = l = i
    }
    ranges << (r == l ? l.to_s : "#{l}->#{r}")
    ranges
end
