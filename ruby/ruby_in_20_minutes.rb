# frozen_string_literal: true

def hi(name="world")
  puts "Hello #{name.capitalize}!"
end

hi 'matz'


class Greeter
  def initialize(name = 'world')
    @name = name
  end

  def say_hi
    puts "Hi #{@name.capitalize}!"
  end
end
greeter = Greeter.new 'chefe'
#puts greeter.name
#puts greeter.@name
p greeter.class.instance_methods
p Greeter.instance_methods
puts greeter.respond_to? :say_hi
puts greeter.respond_to? 'say_hi'
puts greeter.respond_to? 'name'
puts greeter.respond_to? :name
# Classes are objects and can be 'reopened' - monkey patching
class Greeter
  attr_accessor :name
end
puts greeter.respond_to? :name
puts greeter.respond_to? :name=
puts greeter.respond_to? 'name='
puts greeter.name
greeter.name = 'violeta'
puts greeter.name

