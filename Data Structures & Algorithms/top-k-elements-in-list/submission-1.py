class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[[]for i in range(len(nums)+1)]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i,c in freq.items():
            ans[c].append(i)
        res=[]
        for i in range(len(ans)-1,0,-1):
            for i in ans[i]:
                res.append(i)
                if len(res)==k:
                    return res
