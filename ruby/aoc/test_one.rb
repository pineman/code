# frozen_string_literal: true

p $LOAD_PATH
require 'minitest/autorun'
require './util'
require './one'

class TestOne < Minitest::Test
  def setup
    @input = get_input 'one'
  end

  def test_part_one
    assert_equal 66_306, part_one(@input)
  end
end
