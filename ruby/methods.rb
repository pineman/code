module Mod1
  def one
    "one"
  end
end

p Mod1.one rescue

module Mod2
  def self.one
    "one"
  end
end

p Mod2.one

module Mod3
  # TODO: research << (opens singleton class)
  class << self
    def one
      "one"
    end
  end
end

p Mod3.one

module Mod4
  def one
    "one"
  end
end

p Mod4.extend(Mod4).one

module Mod5
  extend self
  def one
    "one"
  end
end

p Mod5.one

module Mod6
  module_function
  def one
    "one"
  end
end

p Mod6.one
