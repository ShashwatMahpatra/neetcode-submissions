class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char1={}
        char2={}
        for i in s:
            char1[i]=char1.get(i,0)+1
        for j in t:
            char2[j]=char2.get(j,0)+1
        return char1==char2