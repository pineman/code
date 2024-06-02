$i = 0
def my_long_method
  $i += 1
  exit if $i > 3
  puts Thread.current.backtrace.class
  puts Thread.current.backtrace.grep(/my_long_method/).count
  a
end

def a
  my_long_method
end

a
