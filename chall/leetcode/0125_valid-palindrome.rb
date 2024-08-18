# @param {String} s
# @return {Boolean}
def is_palindrome(s)
  s = s.downcase.gsub(/[^0-9a-z]/, "")
  l, r = 0, s.size - 1
  while l < r
    return false if s[l] != s[r]
    l += 1
    r -= 1
  end
  true
end
