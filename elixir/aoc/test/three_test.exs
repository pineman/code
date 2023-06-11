defmodule Aoc.Three.Test do
  use ExUnit.Case

  setup_all do
    %{input: Aoc.get_input("three")}
  end

  describe "AoC 2022 day three" do
    test "part one", %{input: input} do
      assert Aoc.Three.part_one(input) == 8105
      assert Aoc.Three.part_one_set(input) == 8105

      Benchee.run(%{
        "normal" => fn -> Aoc.Three.part_one(input) end,
        "set" => fn -> Aoc.Three.part_one_set(input) end
      })
    end

    test "part two", %{input: input} do
      assert Aoc.Three.part_two(input) == 2363
      assert Aoc.Three.part_two_set(input) == 2363

      Benchee.run(%{
        "normal" => fn -> Aoc.Three.part_two(input) end,
        "normal metaprogramming priority" => fn -> Aoc.Three.part_two_meta(input) end,
        "set" => fn -> Aoc.Three.part_two_set(input) end
      })

      # conclusions:
      #  - pattern matching "overloading" functions are not slow whatsoever,
      #    contrary to prediction
      # - sets are still slower as predicted!
    end
  end
end
