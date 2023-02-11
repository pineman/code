p self

public def hi
  'hi'
end
p Object.hi
p Object.new.hi

p BasicObject.hi
p Kernel.hi

class A
  def self.a
    'hi'
  end
end
A.a
#A.new.a

module B
  def b
    'hi'
  end
end

class C
  include B
end
C.new.b

class Module
  def new
    Object.new.extend(self)
  end
end
p B.new.b

