# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
    s.chars.tally == t.chars.tally
end
