# @param {String} s
# @return {Integer}
T = {
  "I" => 1,
  "IV" => 4,
  "V" => 5,
  "IX" => 9,
  "X" => 10,
  "XL" => 40,
  "L" => 50,
  "XC" => 90,
  "C" => 100,
  "CD" => 400,
  "D" => 500,
  "CM" => 900,
  "M" => 1000
}
def roman_to_int(s)
  t = 0
  l = 0
  p s
  while l < s.size
  if T[s[l..l+1]]
    v = T[s[l..l+1]]
    l += 2
  else
    v = T[s[l]]
    l += 1
  end
  p v
  t += v
  end
  t
end
