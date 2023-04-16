module Logging
  def log(level, message)
    File.open("log.txt", "a") do |f|
      f.write "#{level}: #{message}"
    end
  end
end

class Service < String
  include Logging

  def do_something
    begin
      # do something
    rescue StandardError => e
      log :error, e.message
    end
  end
end

p Service.ancestors
