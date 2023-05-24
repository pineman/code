defmodule Aoc.One.Test do
  use ExUnit.Case

  test "AoC 2022 day one" do
    input = Aoc.get_input("one")
    assert Aoc.One.part_one(input) == 66_306
    assert Aoc.One.part_two(input) == 195_292
  end
end
