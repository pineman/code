# frozen_string_literal: true

def block_cenas
  puts 'enter block_cenas'
  yield
  puts 'leave block_cenas'
end
block_cenas { puts 'olá' }

module ToFile
  def filename
    "object_#{object_id}.txt"
  end

  def to_f
    File.open(filename, 'w') { |f| f.write(to_s) }
  end
end

class Person
  include ToFile
  attr_accessor :name

  def initialize(name)
    @name = name
  end

  def to_s
    name
  end
end
Person.new('matz').to_f

a = [5, 3, 4, 1].sort
a.any? { |i| i > 6 }
a.any? { |i| i > 4 }
a.all? { |i| i > 4 }
a.all?(&:positive?)
a.map { |x| x**2 }
# collect is an alias for map
a.collect { |i| i * 2 }
a.select(&:even?)
a.select(&:odd?)
a.max
a.member? 2
puts a
puts "[#{a.join(', ')}]"
p a
a.inject { |t, i| t * i }
a.inject do |sum, i|
  puts "sum: #{sum} i: #{i} sum + i: #{sum + i}"
  sum + i
end

# https://rubyapi.org/3.0/o/file#method-c-open
# With no associated block, File.open is a synonym for File.new. If the optional code block is given, it will be passed the opened file as an argument and the File object will automatically be closed when the block terminates.
a = {a: 1, b: 2}
p a
a.each { |k, v| p(k, v) }
a.each_key { |k| p k }
a.each_value { |v| p v }
Array.new(4) { |i| i + 1 }
Array.new(4, &:to_s)
# well, tens push e pop - stack.
# com shift e unshift tens uma FIFO