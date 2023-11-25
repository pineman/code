class A
  def self.a
    @a ||= "test"
    @a
  end
end

p A.a()
p A.a()
p A.a()
