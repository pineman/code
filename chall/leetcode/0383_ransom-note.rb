# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
  m = magazine.chars.tally
  return false if ransom_note.chars.tally.find { |char, c| !m[char] || m[char] < c }
  true
end
