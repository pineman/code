require 'json'
require 'async'
require 'async/http/internet'

Async do
  internet = Async::HTTP::Internet.new
  headers = [
    ["User-Agent", "Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.12026; Pro"],
    ["Accept", "application/json"],
  ]
  response = internet.get("https://outlook.office365.com/autodiscover/autodiscover.json/v1.0/randomstring.jmoyer@authentic.com?Protocol=ActiveSync", headers)
  pp response
  pp JSON.parse(response.read)
ensure
  internet.close
end
