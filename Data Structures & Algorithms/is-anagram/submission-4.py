class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        hashmap_s,hashmap_t=defaultdict(int),defaultdict(int)

        for i in range(len(s)):
            hashmap_s[s[i]]+=1
            hashmap_t[t[i]]+=1

        for c in hashmap_s:
            if hashmap_s[c]!=hashmap_t[c]:
                return False
        return True

        
        
    
        

        
        
        