defmodule AocTest do
  use ExUnit.Case
  doctest Aoc

  test "day one part one" do
    assert Aoc.part_one() == 66_306
  end
end
