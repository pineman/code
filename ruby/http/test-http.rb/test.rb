require 'json'
require 'http'

b = HTTP.follow.get('https://hacker-news.firebaseio.com/v0/item/8863.json').body.to_s
p JSON.parse(b)
