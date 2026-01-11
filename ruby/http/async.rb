require "async"

require "excon"
require "httpx"
require "curb"
require "typhoeus"
require "http"
require "net/http"

start = Time.now

Async do
  tasks = []
  20.times do |i|
    tasks << Async do
      #HTTP.get("https://httpbin.org/delay/1")
      #URI.open("https://httpbin.org/delay/1")
      #Net::HTTP.get(URI("https://httpbin.org/delay/1"))
      #HTTPX.get("https://httpbin.org/delay/1")
      #Excon.get("https://httpbin.org/delay/1")
      #Typhoeus.get("https://httpbin.org/delay/1")
      Curl.get("https://httpbin.org/delay/1")
    end
  end
  tasks.each(&:wait)
end.wait

puts Time.now - start
