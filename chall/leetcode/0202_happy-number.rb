# @param {Integer} n
# @return {Boolean}
# Kinda dubious what a "cycle" is. I'm not 100% sure this equation is injective, but alas let's assume it is
def is_happy(n)
    prev = Hash.new(false)
    loop do
        m = n.to_s.chars.map(&:to_i).sum { _1 ** 2 }
        return true if m == 1
        return false if prev[m]
        prev[m] = true
        n = m
    end
end
