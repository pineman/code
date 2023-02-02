# frozen_string_literal: true

x = y = 0
x += 1 while x < 10
x = 2 unless y == 3
x -= 1 until x.zero?
puts 'everything but nil and false is true, including the integer 0!'

a = 'cenas bro'
b = ->(arg) { puts arg }
b.call a

array = [1, 2, 3, 4]
array.each { |e| puts e }

i = 'Hello, Ruby,'.index('Ruby')
puts i

puts 'cenas bro'.sub(/[aeiou]/, '*')
puts 'cenas bro'.gsub(/[aeiou]/, '*')
10.times { |x| puts "sentence #{x + 1}" }
10.times { puts 'ello' }
