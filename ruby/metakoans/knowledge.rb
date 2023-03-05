$block = nil
class Module
  def attribute(a, &b)
    case a
    when String
      class_eval("
        attr_accessor :#{a}
        def #{a}?
          #{a} != nil
        end
       ")
      if block_given?
        $block=b
        class_eval("
        def initialize
          @#{a} = instance_eval(&$block)
        end
      ")
      end
    when Hash
      k, v = a.keys[0], a.values[0]
      class_eval("
        attr_accessor :#{k}
        def #{k}?
          #{k} != nil
        end
        def initialize
          @#{k}=#{v}
        end
        @#{k}=#{v}
      ")
    else
      raise ArgumentError
    end
  end
end
