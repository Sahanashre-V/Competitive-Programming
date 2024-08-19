class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        s1_chars = {}
        for char in s1:
            s1_chars[char] = s1_chars.get(char, 0) + 1
        
        window_size = len(s1)
        for i in range(len(s2) - window_size + 1):
            window = s2[i:i+window_size]
            window_chars = {}
            for char in window:
                window_chars[char] = window_chars.get(char, 0) + 1
            
            if window_chars == s1_chars:
                return True
        
        return False