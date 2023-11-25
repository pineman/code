class A
  def m(a:, b:)
    p a, b
  end
end

o = {a:1,b:2,c:3}
p A.new.m(**o)
