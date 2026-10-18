class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=bin(n)[2:].count('1')
        return ans
        