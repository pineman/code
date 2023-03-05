class Module
  def attribute(name, &block)
    self.module_eval "instance_eval(&block)"
    self.module_eval { instance_eval(&block) }
  end
end

c = Class.new {
  self.attribute("hoge") { puts "katamari" }
}

