class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            cs = {}
            ct = {}
            
            for i in range (len(s)):
                cs[s[i]] = 1 + cs.get(s[i],0)
                ct[t[i]] = 1 + ct.get(t[i],0)
                
            for j in cs:
                if cs[j] != ct.get(j,0):
                    return False
            return True
        
        return False