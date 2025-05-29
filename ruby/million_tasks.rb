# run with \gtime -v ruby million_tasks.rb to see max rss
require 'async'
require 'async/barrier'

barrier = Async::Barrier.new
Async do
  1_000_000.times.to_a.map {
    barrier.async {
      sleep 2
    }
  }
  barrier.wait
end
