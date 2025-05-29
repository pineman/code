# benchmark_string_vs_regex.rb
# Compare String#include? vs. a pre-compiled Regexp on the same data
#
# ▸ Ruby ≥ 3.1 ships with benchmark/ips in stdlib
# ▸ Run with:  ruby benchmark_string_vs_regex.rb

require 'benchmark/ips'

# -------------------------------------------------------------------
# Test data
# -------------------------------------------------------------------
HAYSTACK_LENGTH = 2_000
NEEDLE_LENGTH   = 20

# deterministic pseudo-random text so every run is identical
ALPHABET = ('a'..'z').to_a.freeze
haystack = Array.new(HAYSTACK_LENGTH) { ALPHABET.sample }.join
needle   = haystack[(HAYSTACK_LENGTH / 2), NEEDLE_LENGTH] # guaranteed hit

# pre-compile the regexp once
needle_re = Regexp.new(Regexp.escape(needle))

puts "Ruby version : #{RUBY_VERSION} (#{RUBY_RELEASE_DATE})"
puts "Haystack len : #{haystack.bytesize}"
puts "Needle len   : #{needle.bytesize}"
puts "-" * 50

Benchmark.ips do |x|
  x.report('String#include?')    { haystack.include?(needle) }
  x.report('pre-compiled Regexp') { haystack.match?(needle_re) }

  x.compare!
end
