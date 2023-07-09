require 'json'
require 'faraday'
require 'faraday_middleware'

f = Faraday.new do |f|
  f.use FaradayMiddleware::FollowRedirects
end
b = f.get('https://hacker-news.firebaseio.com/v0/item/8863.json').body
p JSON.parse(b)
