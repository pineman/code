require 'json'
require 'httparty'

b = HTTParty.get('https://hacker-news.firebaseio.com/v0/item/8863.json').body
p JSON.parse(b)

