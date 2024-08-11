# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
  return "" if strs.any? { _1.empty? }
  return strs[0] if strs.size == 1
  min = strs.map(&:size).min
  cc = 0
  while strs.all? { _1.start_with?(strs[0][..cc]) } && cc < min
    cc += 1
  end
  strs[0][...cc]
end
