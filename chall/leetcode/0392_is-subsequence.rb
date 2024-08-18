# @param {String} s
# @param {String} t
# @return {Boolean}
def is_subsequence(s, t)
  return true if s.empty? || s == t
  return false if t.empty?
  i = 0
  j = 0
  n = 0
  while i < s.size
    if s[i] == t[j]
      n += 1
      i += 1
    end
    return true if n == s.size
    j += 1
    break if j == t.size
  end
  false
end
# make tab of set of t chars indexed by the ascii value with 0/1 if char present in t
# early out if any char of s not in there
