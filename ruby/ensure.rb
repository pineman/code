def m
  while 1
    begin
      1/0
    rescue
      return
    ensure
      p 'ensure'
    end
  end
end
m
