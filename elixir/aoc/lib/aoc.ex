defmodule Aoc do
  # File.read/1 vs File.read!/1 https://elixir-lang.org/getting-started/try-catch-and-rescue.html#errors
  def get_input(day) do
    File.read!("input/#{day}")
    |> String.split("\n")
    |> Enum.drop(-1)
  end
end
