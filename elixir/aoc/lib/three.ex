defmodule Aoc.Three do
  def run do
    input = Aoc.get_input("three")
    IO.puts(part_one(input))
    IO.puts(part_two(input))
  end

  defp split_rucksack(rucksack) do
    rucksack
    |> String.split_at(div(String.length(rucksack), 2))
    |> Tuple.to_list()
    |> Enum.map(&String.graphemes/1)
  end

  defp get_first_common([first, second]) do
    first
    |> Enum.find(&(&1 in second))
    |> String.to_charlist()
    |> Enum.at(0)
  end

  defp map_priority(common) do
    if common >= ?a do
      common - ?a + 1
    else
      common - ?A + 27
    end
  end

  def part_one(input) do
    input
    |> Enum.map(fn rucksack ->
      rucksack
      |> split_rucksack()
      |> get_first_common()
      |> map_priority()
    end)
    |> Enum.sum()
  end

  def part_two(input) do
    nil
  end
end
