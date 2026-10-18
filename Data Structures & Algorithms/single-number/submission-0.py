class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp={}
        ans=0
        for i in nums:
            mp[i]=mp.get(i,0)+1
        for num,frequency in mp.items():
            if frequency==1:
                ans=num
        return ans