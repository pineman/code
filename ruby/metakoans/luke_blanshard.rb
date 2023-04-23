style = :code # or :string

case style
when :string
  class Module
    def attribute desc, &block
      if desc.is_a? Hash
        name = desc.keys[0]
        default = desc[name]
        raise "Hash or block, not both" if block
      else
        name, default = desc, nil
      end
      module_eval <<-"end;", __FILE__, __LINE__
        def #{name}?; #{name} != nil end            # Permanent definition of query method
        def __#{name}__ivarget;   @#{name}   end    # ivar getter and setter
        def __#{name}__ivarset v; @#{name}=v end
                                                            # Initial def of attr reader
        define_method(name) { self.#{name} = (block ? instance_eval(&block) : default) }
        def #{name}= value                                  # Initial def of attr writer
          (class << self; self; end).class_eval do
            alias_method :#{name},  :__#{name}__ivarget     # Subsequent calls use ivar getter and setter
            alias_method :#{name}=, :__#{name}__ivarset
          end
          @#{name} = value
        end
      end;
    end
  end

when :code
  class Module
    def attribute desc, &block
      if desc.is_a? Hash
        name = desc.keys[0]
        default = desc[name]
        raise "Hash or block, not both" if block
      else
        name, default = desc, nil
      end
      ivar_name = "@#{name}"
      module_eval do
        define_method("#{name}?") {send(name) != nil}
        define_method("__#{name}__ivarget") {    instance_variable_get(ivar_name) }
        define_method("__#{name}__ivarset") {|v| instance_variable_set(ivar_name, v) }
        define_method(name) { send("#{name}=", block ? instance_eval(&block) : default) }
        define_method("#{name}=") do |value|
          (class << self; self; end).class_eval do
            alias_method "#{name}",  "__#{name}__ivarget"
            alias_method "#{name}=", "__#{name}__ivarset"
          end
          instance_variable_set(ivar_name, value)
        end
      end
    end
  end
end
