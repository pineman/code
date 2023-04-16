class A
  attr_accessor :a
  def asdf
    a = 2
  end
end
a = A.new
a.asdf
p a.a
