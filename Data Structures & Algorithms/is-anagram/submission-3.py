class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map_s,map_t={},{} #create hashmap for s & t
        
        for i in range(len(s)):
            map_s[s[i]]=1+map_s.get(s[i],0)   #building the hashmap for s
            map_t[t[i]]=1+map_t.get(t[i],0)   #building the hashmap for t
        
        for c in map_s:
            if map_s[c]!=map_t.get(c,0):
                return False
        return True
        
        