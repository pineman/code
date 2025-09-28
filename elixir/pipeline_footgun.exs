# https://github.com/elixir-lang/elixir/pull/14795
defmodule PipelineTest do
  def fetch_users do
    IO.puts("Fetching users...")
    [
      %{id: 1, name: "Alice", active: true},
      %{id: 2, name: "Bob", active: false},
      %{id: 3, name: "Charlie", active: true}
    ]
  end

  def validate_data(users) do
    IO.puts("Validating data...")
    raise "Validation failed: Invalid user format"
    users
  end

  def process_results(users) do
    IO.puts("Processing results...")
    active_users = Enum.filter(users, & &1.active)
    IO.puts("Found #{length(active_users)} active users")
    active_users
  end
end

# Now you can test the pipeline with the syntax error:
PipelineTest.fetch_users()
|> PipelineTest.validate_data(data]  # missing open bracket - syntax error
|> PipelineTest.process_results()

