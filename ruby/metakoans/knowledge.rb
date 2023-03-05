$block = nil
def attribute a, &b
  if a.class == String
    class_eval("attr_accessor :#{a}; def #{a}?; #{a} != nil; end")
  elsif a.class == Hash
    class_eval("
def initialize
  @#{a.keys[0]}=#{a.values[0]}
end
def #{a.keys[0]}
  @#{a.keys[0]}
end
def #{a.keys[0]}= v
  @#{a.keys[0]}=v
end
def #{a.keys[0]}?
  #{a.keys[0]} != nil
end
")
  end
  if block_given?
    $block = b
    class_eval("
def initialize
  @a=instance_eval &$block
end
")
  end
end
