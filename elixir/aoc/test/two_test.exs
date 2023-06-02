defmodule Aoc.Two.Test do
  use ExUnit.Case

  setup_all do
    %{input: Aoc.get_input("two")}
  end

  describe "AoC 2022 day two" do
    test "part one", %{input: input} do
      assert Aoc.Two.part_one(input) == 8_933
    end

    test "part two", %{input: input} do
      assert Aoc.Two.part_two(input) == 11_998
    end
  end
end
