module Test
  class << self
    CONST = 1
  end
end

p Test.singleton_class::CONST
p Test::CONST
