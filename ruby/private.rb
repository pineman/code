class A
  def hi
    'hi'
  end
  protected :hi
end

class B < A
  def hello
    hi
  end
end

b = B.new
#p b.hi
def b.bypass
  hi
end
p b.bypass
