defmodule Aoc.DayOne do
  def run do
    input = Aoc.get_input("one")
    IO.puts(part_one(input))
    IO.puts(part_two(input))
  end

  defp elves(input) do
    input
    |> Enum.chunk_by(&(&1 == ""))
    |> Enum.filter(&(&1 != [""]))
    |> Enum.map(fn elf ->
      Enum.map(elf, &String.to_integer/1)
    end)
    |> Enum.map(&Enum.sum/1)
    |> Enum.sort()
  end

  def part_one(input) do
    elves(input)
    |> Enum.max
  end

  def part_two(input) do
    elves(input)
    |> Enum.slice(-3..-1)
    |> Enum.sum()
  end
end
