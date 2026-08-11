class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #freq={}
        #for i in nums:
         #   freq[i]=freq.get(i,0)+1
           # if freq[i]>1:
            #    return True
       # return False
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False