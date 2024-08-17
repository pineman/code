class Cena
  A = 1
  class << self
    B = 2
  end

  def instance_method
    p A # works
    # p B  # doesn't work, needs self.class
    p self.class.B # works
  end

  def self.class_method
    p A # works
    p B # works
  end
end

p Cena::A
p Cena.B
# p Cena::B # doesn't work with namespace resolution ::

Cena.new.instance_method # works for A, needs self.class.B for B
Cena.class_method # works for both A and B

p Cena.constants # [:A]
p Cena.singleton_class.constants # [:B]
