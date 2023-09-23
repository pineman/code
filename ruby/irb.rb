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
  bak = $VERBOSE
  $VERBOSE = nil
  load file
  $VERBOSE = bak
end

def watch_and_reload(dir_path)
  trap('INT', 'IGNORE')
  listener = Listen.to(File.dirname(dir_path), only: /\.rb$/) do |modified, added, removed|
    (modified + added).each do |file|
      reload file
    end
    # 'unload' does not exist for removed...
  end
  listener.start
end

if ARGV.count != 1
  STDERR.puts <<EOS
Usage: irb.rb <dir to watch>
Launch irb and auto-reload all files in dir for ultimate REPL prototyping à la rails console.
Run with e.g. 'GEM_PATH=gems/ruby/3.2.0:' if using vendored gems
EOS
  exit 1
end

dir = ARGV[0].dup
Dir.glob("#{dir}/*.rb").map { reload _1 unless _1.include?("test") }
Thread.new { watch_and_reload(dir) }

ARGV.clear
IRB.start
