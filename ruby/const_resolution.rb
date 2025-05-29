module Test
  CONSTA = 1
  class << self
    def ma
      CONSTA
    end
    CONST = 1
    def m
      CONST
    end
  end
end

p Test::CONSTA
p Test.ma
p Test.singleton_class::CONST
p Test.m
p Test::CONST
