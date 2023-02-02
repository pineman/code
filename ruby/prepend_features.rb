def test(object, method)
  object.public_send method
rescue => e
  p e
end
test Module.new, :puts
test Module, :puts
test Module.new, :prepend_features
# 'undefined' when it's actually private:
test Module, :prepend_features

