def m
  Async do
    a = Async do
      r = rand()
      puts "a #{r}"
      if r < 0.5
        return true
      end
      false
    end.wait
    b = Async do
      r = rand()
      puts "b #{r}"
      if r < 0.8
        return true
      end
      false
    end.wait
    a || b
  end.wait
end

start = Time.now_monotonic
m
puts Time.now_monotonic - start
