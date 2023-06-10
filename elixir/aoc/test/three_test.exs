defmodule Aoc.Three.Test do
  use ExUnit.Case

  setup_all do
    %{input: Aoc.get_input("three")}
  end

  describe "AoC 2022 day three" do
    test "part one", %{input: input} do
      assert Aoc.Three.part_one(input) == 8105
    end

    test "part two", %{input: input} do
      assert Aoc.Three.part_two(input) == 2363
    end
  end
end
