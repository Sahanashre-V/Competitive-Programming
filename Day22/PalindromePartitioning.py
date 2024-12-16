def partition(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s): 
            result.append(path[:])
            return

        for end in range(start, len(s)):
            if is_palindrome(s[start:end + 1]):  
                path.append(s[start:end + 1]) 
                backtrack(end + 1, path)       
                path.pop()                  

    result = []
    backtrack(0, [])
    return result
