# frozen_string_literal: true

require 'hello'

RSpec.describe 'Hello' do
  describe MegaGreeter do
    it 'says hi to chefe by default' do
      mg = described_class.new
      expect(mg.names).to eq 'chefe'
    end
  end
end
