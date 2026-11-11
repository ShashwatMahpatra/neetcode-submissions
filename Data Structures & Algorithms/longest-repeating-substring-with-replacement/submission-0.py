class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res={}
        maximum=0
        l=0
        ans=0
        for i in range(len(s)):
            res[s[i]]=res.get(s[i],0)+1
            maximum=max(maximum,res[s[i]])
            while(i-l+1)-maximum>k:
                res[s[l]]-=1
                l+=1
            ans=max(maximum,i-l+1)
        return  ans
        