defmodule Aoc.DayOne.Test do
  use ExUnit.Case

  test "2022 Day One" do
    input = Aoc.get_input("one")
    assert Aoc.DayOne.part_one(input) == 66_306
    assert Aoc.DayOne.part_two(input) == 195_292
  end
end
