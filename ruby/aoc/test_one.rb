# frozen_string_literal: true

require 'minitest/autorun'
require './util'
require './one'

class TestOne < Minitest::Test
  def setup
    @input = get_input('one')
  end

  def test_part_one
    assert_equal 66_306, part_one(@input)
  end

  def test_part_two
    assert_equal 195_292, part_two(@input)
  end
end
