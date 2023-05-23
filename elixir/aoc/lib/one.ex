defmodule Aoc do
  def part_one do
    File.read("input/one")
    |> elem(1)
    |> String.split("\n")
    |> Enum.chunk_by(&(&1 == ""))
    |> Enum.filter(&(&1 != [""]))
    |> Enum.map(fn elf ->
      Enum.map(elf, &String.to_integer/1)
    end)
    |> Enum.map(&Enum.sum/1)
    |> Enum.max()
  end
end
