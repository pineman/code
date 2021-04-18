current_process = self()

# Spawn an Elixir process (not an operating system one!)
spawn_link(fn ->
	Process.send_after current_process, {:msg, "hello world"}, 1_000
end)

# Block until the message is received
receive do
	{:msg, contents} -> IO.puts contents
end
