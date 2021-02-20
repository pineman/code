# frozen_string_literal: true

require 'hello'

RSpec.describe 'Hello' do
  describe Greeter do
    it 'says hi to chefe by default' do
      greeter = described_class.new
      expect(greeter.name).to be 'chefe'
    end
  end
end
