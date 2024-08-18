# @param {String} s
# @param {String} t
# @return {Boolean}
def is_isomorphic(s, t)
  h = {}
  (0...s.size).each { |i|
    if !h.key?(s[i])
      h[s[i]] = t[i]
    elsif h[s[i]] != t[i]
      return false
    end
  }
  return false if h.values.size != h.values.uniq.size
  true
end
