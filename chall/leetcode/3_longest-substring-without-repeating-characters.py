class Solution:
    #def lengthOfLongestSubstring(self, s: str) -> int:
    #    n = len(s)
    #    m = 0
    #    for i in range(n):
    #        for k in range(i, n):
    #            if k-i+1 > len(set(s[i:k+1])):
    #                break
    #            if k-i+1>m:
    #                m=k-i+1
    #    return m
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     sub = ''
    #     m = 0
    #     for c in s:
    #         if c in sub:
    #             sub = sub[sub.index(c)+1:]
    #         sub += c
    #         n = len(sub)
    #         if n > m:
    #             m = n
    #     return m
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = m = 0
        for r in range(len(s)):
            u = len(set(s[l:r+1]))
            if u < len(s[l:r+1]):
                l+=1
                while s[l] != s[r]:
                    l+=1
            if u > m:
                m = u
        return m


import unittest
class TestSolution(unittest.TestCase):
    def testLengthOfLongestSubstring(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring(''), 0)
        self.assertEqual(s.lengthOfLongestSubstring(' '), 1)
        self.assertEqual(s.lengthOfLongestSubstring('au'), 2)
        self.assertEqual(s.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(s.lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(s.lengthOfLongestSubstring('pwwkew'), 3)


if __name__ == '__main__':
    unittest.main()
