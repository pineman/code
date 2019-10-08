defmodule Types do
  import IO

  def numbers do
    puts 0xFF
    puts 1.0e-3
    puts 4/2
    puts div 4, 2 # Integer division, comes from Kernel.* (the Kernel is autoimported)
    puts rem 5, 2 # Modulo operation
    puts 1_000_000
  end

  def atoms do
    puts :an_atom
    puts :"a spacy atom"
    # Atoms are like enums. It has two parts: the text (name of the atom) and the
    # value (opaque), which is a reference to the atom table.
    a = :atom
    # the variable `a` only contains the atom's value (a reference to the atom
    # table), not the full text of the atom.

    # Another syntax for atoms, using aliases:
    AnAtom
    puts AnAtom == :"Elixir.AnAtom"
    # At compile time its transformed to :"Elixir.AnAtom". Aliases are automatically
    # prefixed with 'Elixir', only if the prefix doesn't already exist.
    # So, this is valid:
    puts AnAtom == Elixir.AnAtom

    alias IO, as: MyIO
    puts MyIO == Elixir.IO
  end

  def booleans do
    # Booleans are atoms! As syntactic sugar, you can reference the
    # :true and :false atoms without the colons:
    puts :true == true
    puts :false == false

    # The logical operators only work on the :true and :false atoms:
    puts true and :false
    puts :true or false
    puts not false
    #puts not :an_atom # Error!

    # Another special atom is :nil (or nil).
    # Only :false or :nil are 'falsy'.

    # Logical short-circuit operators: ||, &&, !
    # || returns the first expression that isn't falsy.
    # && returns the second expression only if the first one is truthy.
    # Otherwise, it does not evaluate the second expression, and returns the first.
    # Short-circuiting can be used for elegant operation chaining. For example, if you need to fetch a value from cache, a local disk, or a remote database, you can do something like this:
    # read_cached || read_from_disk || read_from_database
    # Similarly, you can use the operator && to ensure that certain conditions are met:
    # database_value = connection_established? && read_data
    # In both examples, short-circuit operators make it possible to write concise code with- out resorting to complicated nested conditional constructs.
    puts true || nil
    puts false && nil
  end

  # Data structures are immutable
  def tuples do
    # https://hexdocs.pm/elixir/Tuple.html
    # Tuples are appropriate for grouping small, fixed number of elements together.
    puts {"Bob", 25, :male}
  end

  def lists do
    # https://hexdocs.pm/elixir/List.html
    # Singly linked list. Recursive
    p = [1,2,3,4]

    [1] == [1 | []] # a proper list's last element tail is the empty list.
    # Here's an improper list:
    [p | 5] # This is an improper list. The tail isn't a list itself.

    [5 | p] # push to head O(1)
    puts hd(p) # head of list is a VALUE
    puts tl(p) # tail of list is a LIST (or a value if the list is improper)

    puts p == [1,2,3,4] # p is not modified.

    p ++ [5] # ++ concatenates lists. O(n).
    # here's a stupid way to do it:
    List.flatten [p | [5]]

    # `in` operator: O(n)
    puts 5 in p

    puts p ++ [6,7,8]
    puts p -- [1,5,7] # subtract lists
  end

  def maps do
    empty_map = %{}
    squares = %{1 => 1, 2 => 4, 3 => 9}
    squares = Map.new([{1, 1}, {2, 4}, {3, 9}])
    IO.inspect squares[2] # https://hexdocs.pm/elixir/IO.html#inspect/2
    squares[5] |> IO.inspect
    IO.inspect Map.get(squares, 5, :not_found), label: "test"
    # Is the value on the map nil or :not_found ????
    # solution: use Map.fetch, or Map.fetch! to raise an exception on key not found.
    IO.inspect Map.fetch(squares, 2)
    IO.inspect Map.fetch(squares, 5)

    # Maps with atom keys have special syntax. keys go from :name to name:,
    # and you can access fields with mapname.field
    bob = %{name: "Bob", age: 25, works_at: "Initech"}
    IO.inspect bob.name

    # Map update syntax. Only works on already existing fields
    bob = %{bob | age: "26", works_at: "Celfocus"}
  end
end
