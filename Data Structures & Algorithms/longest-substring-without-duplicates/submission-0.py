class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSt=set()
        l,res=0,0

        for r in range(len(s)):
            while s[r] in charSt :
                charSt.remove(s[l])
                l+=1
            charSt.add(s[r])
            res=max(res,r-l+1)
        
        return res
        