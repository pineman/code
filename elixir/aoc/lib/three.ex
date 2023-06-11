defmodule Aoc.Three do
  def run do
    input = Aoc.get_input("three")
    # IO.puts(part_one(input))
    IO.puts(part_two(input))
  end

  defp map_priority(item) do
    if item >= ?a do
      item - ?a + 1
    else
      item - ?A + 27
    end
  end

  def part_one(input) do
    input
    |> Enum.map(fn rucksack ->
      rucksack
      |> String.to_charlist()
      |> (&Enum.split(&1, div(length(&1), 2))).()
      |> (fn {a, b} -> Enum.find(a, &(&1 in b)) end).()
      |> map_priority()
    end)
    |> Enum.sum()
  end

  def part_two_set(input) do
    input
    |> Enum.chunk_every(3)
    |> Enum.map(fn x ->
      x
      |> Enum.map(&String.to_charlist/1)
      |> Enum.map(&MapSet.new/1)
      |> (fn [a, b, c] ->
            a
            |> MapSet.intersection(b)
            |> MapSet.intersection(c)
            |> Enum.at(0)
          end).()
      |> map_priority()
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
      |> map_priority()
    end)
    |> Enum.sum()
  end
end
