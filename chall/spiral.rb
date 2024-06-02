require "minitest/autorun"

def nth_odd_number(n)
  2 * n + 1
end

Spiral = Struct.new(:m, :size, :number_size)

def subspiral(s, i)
  r, c = [s.size / 2 - i, s.size / 2 + i]
  if i == 0
    s.m[r][c] = 1
    return
  end

  sub_spiral_size = nth_odd_number(i)
  num = nth_odd_number(i - 1)**2
  (sub_spiral_size - 1).times do
    num += 1
    r += 1
    s.m[r][c] = num
  end
  (sub_spiral_size - 1).times do
    num += 1
    c -= 1
    s.m[r][c] = num
  end
  (sub_spiral_size - 1).times do
    num += 1
    r -= 1
    s.m[r][c] = num
  end
  (sub_spiral_size - 1).times do
    num += 1
    c += 1
    s.m[r][c] = num
  end
end

def spiral(upto)
  size = Math.sqrt(upto).ceil
  size += 1 if size % 2 == 0
  number_size = (size**2).to_s.size
  m = size.times.map { size.times.map { 0 } }
  spiral = Spiral.new(m:, size:, number_size:)
  (size / 2 + 1).times do |i|
    subspiral(spiral, i)
  end
  spiral
end

def print_spiral(spiral)
  spiral.m.each { |row|
    s = ""
    row.each { |c|
      s += sprintf("%2d ", c)
    }
    puts s
  }
end

print_spiral(spiral(26))

class TestSpiral < Minitest::Test
  make_my_diffs_pretty!

  def test_spiral
    # standard:disable Layout/ExtraSpacing
    m = [
      [43, 44, 45, 46, 47, 48, 49],
      [42, 21, 22, 23, 24, 25, 26],
      [41, 20, 7,  8,  9,  10, 27],
      [40, 19, 6,  1,  2,  11, 28],
      [39, 18, 5,  4,  3,  12, 29],
      [38, 17, 16, 15, 14, 13, 30],
      [37, 36, 35, 34, 33, 32, 31]
    ]
    # standard:enable Layout/ExtraSpacing
    expected = Spiral.new(size: 7, number_size: 2, m:)
    assert_equal expected, spiral(26)
  end
end
