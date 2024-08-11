# Definition for a binary tree node.
# class TreeNode
#   attr_accessor :val, :left, :right
#   def initialize(val = 0, left = nil, right = nil)
#     @val = val
#     @left = left
#     @right = right
#   end
# end
# @param {TreeNode} root
# @return {Integer}
def average_of_subtree(root)
  def s(t)
    return {sum: 0, n: 0, m: 0} if t.nil?
    return {sum: t.val, n: 1, m: 1} if !t.left && !t.right
    l = s(t.left)
    r = s(t.right)
    sum = t.val + l[:sum] + r[:sum]
    n = 1 + l[:n] + r[:n]
    m = l[:m] + r[:m]
    m += 1 if t.val == sum / n
    {sum:, n:, m:}
  end
  s(root)[:m]
end
