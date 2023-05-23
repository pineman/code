# frozen_string_literal: true

require './util'

def part_one_tito(input)
  input.chunk { _1.empty? && :_separator }
       .map { _2.sum(&:to_i) }
       .max
end

def elves(input)
  input.chunk(&:empty?).map { _2.sum(&:to_i) }.sort
end

def part_one(input)
  elves(input).last
end

def part_two(input)
  elves(input)[-3..-1].sum
end

if __FILE__ == $0
  input = get_input('one')
  puts part_one(input)
  puts part_two(input)
end
