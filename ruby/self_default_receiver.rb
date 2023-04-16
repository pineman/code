class String
  p self
  def asdf
    # self is default receiver (in this case, the string instance itself)
    p self
    concat('asdf')
  end
end

p ''.asdf
