require "async"
require "excon"
require "httpx"
require "http"
require "curb"
require "typhoeus"

start = Time.now
Async do |task|
  20.times do |i|
    task.async do
      #HTTP.get("https://httpbin.org/delay/1.6")
      #URI.open("https://httpbin.org/delay/1.6")
      #Net::HTTP.get_response(URI("https://httpbin.org/delay/1.6"))
      #HTTPX.get("https://httpbin.org/delay/1.6")
      #Excon.get("https://httpbin.org/delay/1.6")
      #Typhoeus.get("https://httpbin.org/delay/1.6")
      #Curl.get("https://httpbin.org/delay/1.6")
    end
  end
end.wait
puts Time.now - start
