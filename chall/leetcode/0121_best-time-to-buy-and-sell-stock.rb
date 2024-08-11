# @param {Integer[]} prices
# @return {Integer}
# We don't need to return the actual indices, just the max profit possible.
# Therefore, we don't need to worry about cases like [8,10,1,9] where max
# happens before min; and which direction we should go then (left or right?)
# Alternate view: we need to sell some day. if we want to sell at i'th position,
# we need to buy at minimum value from previous i - 1. keep a minimum till here.
def max_profit(prices)
  return 0 if prices.size == 1
  buy = prices[0]
  max_profit = 0
  prices.each { |v|
    if v < buy
      buy = v
    elsif max_profit < v - buy
      max_profit = v - buy
    end
  }
  max_profit
end
