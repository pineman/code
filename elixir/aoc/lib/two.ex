defmodule Aoc.Two do
  def run do
    input = Aoc.get_input("two")
    IO.puts(part_one(input))
    IO.puts(part_two(input))
  end

  # Most solutions online seem to use pattern matching on function arguments.
  def part_one(input) do
    Enum.map(input, fn x ->
      shape = String.at(x, 2)
      outcome = @inferOutcomeMap[x]
      score(outcome, shape)
    end)
    |> Enum.sum()
  end

  def part_two(input) do
    Enum.map(input, fn x ->
      shape = @inferShapeMap[x]
      outcome = String.at(x, 2)
      score(outcome, shape)
    end)
    |> Enum.sum()
  end

  defp score(outcome, shape) do
    @scoreOutcomeMap[outcome] + @scoreShapeMap[shape]
  end

  @scoreOutcomeMap %{
    "X" => 0,
    "Y" => 3,
    "Z" => 6
  }

  @inferOutcomeMap %{
    "A X" => "Y",
    "A Y" => "Z",
    "A Z" => "X",
    "B X" => "X",
    "B Y" => "Y",
    "B Z" => "Z",
    "C X" => "Z",
    "C Y" => "X",
    "C Z" => "Y"
  }

  @scoreShapeMap %{
    "X" => 1,
    "Y" => 2,
    "Z" => 3
  }

  @inferShapeMap %{
    "A X" => "Z",
    "A Y" => "X",
    "A Z" => "Y",
    "B X" => "X",
    "B Y" => "Y",
    "B Z" => "Z",
    "C X" => "Y",
    "C Y" => "Z",
    "C Z" => "X"
  }
end
