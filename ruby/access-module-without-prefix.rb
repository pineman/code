module Foo
  class Baz
    def self.baz_method
      2
    end
  end
end

class Foo::Bar
  include Foo
  def self.bar_method
    p self.constants
    Baz.baz_method
  end
end

p Foo::Bar.bar_method
