# frozen_string_literal: true

require 'irb'

=begin
os comentários multiline mais esquisitos
que já viste colega
=end
class Greeter
  def initialize(name = 'chefe')
    @name = name
  end

  def say_hi
    puts "Hi #{@name.capitalize}!"
  end
end

class Greeter
  attr_accessor :name
end

class MegaGreeter
  attr_accessor :names

  def initialize(names = 'chefe')
    @names = names
  end

  # Say hi to everybody
  def say_hi
    if @names.nil?
      puts '...'
    elsif @names.respond_to?('each')
      # @names is a list of some kind, iterate!
      @names.each do |name|
        puts "Hello #{name}!"
      end
    else
      puts "Hello #{@names}!"
    end
  end

  # Say bye to everybody
  def say_bye
    if @names.nil?
      puts '...'
    elsif @names.respond_to?('join')
      # Join the list elements with commas
      puts "Goodbye #{@names.join(', ')}. Come back soon!"
    else
      puts "Goodbye #{@names}. Come back soon!"
    end
  end
end

if __FILE__ == $PROGRAM_NAME
  mg = MegaGreeter.new
  mg.say_hi
  mg.say_bye

  # Change name to be "Zeke"
  mg.names = 'Zeke'
  mg.say_hi
  mg.say_bye

  # Change the name to an array of names
  mg.names = %w[Albert Brenda Charles Dave Engelbert]
  mg.say_hi
  mg.say_bye

  # Change to nil
  mg.names = nil
  mg.say_hi
  mg.say_bye

  x = 0
  x += 1 while x < 10
  x = 2 unless y == 3
  x -= 1 until x.zero?
  puts 'everything but nil and false is true!' if 0

  a = 'cenas bro'
  b = ->(x) { puts x }
  b.call a

  array = [1, 2, 3, 4]
  array.each { |x| puts x }
end
