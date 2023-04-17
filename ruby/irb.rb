#!/usr/bin/env ruby

require 'rubygems'
begin
  gem 'listen'
rescue Gem::LoadError
  Gem.install('listen')
  gem 'listen'
end
require 'listen'
require 'irb'

def reload(file)
  old = $VERBOSE
  $VERBOSE = nil
  load file
  $VERBOSE = old
end

def watch_and_reload(dir_path)
  listener = Listen.to(File.dirname(dir_path), only: /\.rb$/) do |modified, added, removed|
    (modified + added).each do |file|
      reload file
    end
    # 'unload' does not exist for removed...
  end
  listener.start
end

if ARGV.count != 2
  STDERR.puts <<EOS
Usage: irb.rb <main file> <dir to watch>
Launch irb and auto-reload all files in dir for ultimate REPL prototyping à la rails console.
EOS
  exit 1
end
file = ARGV[0].dup
dir = ARGV[1].dup
reload file
Thread.new { watch_and_reload(dir) }
ARGV.clear
IRB.start
