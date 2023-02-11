# frozen_string_literal: true

require './util'

def part_one(input)
  res = []
  while (j = input.index '')
    res << input[0..j-1].sum(&:to_i)
    input.slice!(..j)
  end
  res.max
end

# TODO: investigar Enumerable e Enumerator
def part_one_tito(input)
  input.chunk { _1.empty? && :_separator }
       .map { _2.sum(&:to_i) }
       .max
end

if __FILE__ == $0
  puts part_one get_input 'one'
  puts part_one_tito get_input 'one'
end
