defmodule Aoc.One.Test do
  use ExUnit.Case

  setup_all do
    %{input: Aoc.get_input("one")}
  end

  describe "AoC 2022 day one" do
    test "part one", %{input: input} do
      assert Aoc.One.part_one(input) == 66_306
    end

    test "part two", %{input: input} do
      assert Aoc.One.part_two(input) == 195_292
    end
  end
end
