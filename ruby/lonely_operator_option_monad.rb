class String
  def a
    p 'in a'
    nil
  end

  def b
    p 'in b'
    self
  end
end

p "a".a&.b
