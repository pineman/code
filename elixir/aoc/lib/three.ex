defmodule Aoc.Three do
  def run do
    input = Aoc.get_input("three")
    IO.puts(part_one(input))
    IO.puts(part_two(input))
  end

  defp priority(item) do
    if item >= ?a do
      item - ?a + 1
    else
      item - ?A + 27
    end
  end

  # shamelessly "inspired" by https://github.com/jzimbel/adventofcode-elixir/blob/main/lib/advent_of_code/solution/year_2022/day_03.ex
  defp common_list_priority(strings) do
    strings
    |> Enum.map(&(&1 |> String.to_charlist() |> MapSet.new()))
    |> Enum.reduce(&MapSet.intersection/2)
    |> Enum.at(0)
    |> priority()
  end

  defp split_string_middle(string) do
    <<l::binary-size(div(byte_size(string), 2)), r::binary>> = string
    [l, r]
  end

  def part_one_set(input) do
    input
    |> Enum.map(&(&1 |> split_string_middle() |> common_list_priority()))
    |> Enum.sum()
  end

  def part_two_set(input) do
    input
    |> Enum.chunk_every(3)
    |> Enum.map(&common_list_priority/1)
    |> Enum.sum()
  end

  def part_one(input) do
    input
    |> Enum.map(fn rucksack ->
      rucksack
      |> String.to_charlist()
      |> (&Enum.split(&1, div(length(&1), 2))).()
      |> (fn {a, b} -> Enum.find(a, &(&1 in b)) end).()
      |> priority()
    end)
    |> Enum.sum()
  end

  def part_two(input) do
    input
    |> Enum.chunk_every(3)
    |> Enum.map(fn triple ->
      triple
      |> Enum.map(&String.to_charlist/1)
      |> (fn [a, b, c] ->
            Enum.find(a, fn x ->
              x in b && x in c
            end)
          end).()
      |> priority()
    end)
    |> Enum.sum()
  end
end
