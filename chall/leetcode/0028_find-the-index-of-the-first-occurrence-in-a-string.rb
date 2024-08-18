# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
  i, ni = 0, 0
  while i < haystack.size
    if haystack[i] == needle[ni]
      return i - ni if ni == needle.size - 1
      ni += 1
    elsif ni != 0
      i -= ni
      ni = 0
    end
    i += 1
  end
  -1
end
