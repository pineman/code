# @param {String} pattern
# @param {String} s
# @return {Boolean}
def word_pattern(pattern, s)
    words = s.split(' ')
    return false if pattern.size != words.size
    h = {}
    words.zip(pattern.chars).each { |word, pat|
        if !h.key?(pat)
            h[pat] = word
        else
            return false if h[pat] != word
        end
    }
    return false if h.values.size != h.values.uniq.size
    true
end
