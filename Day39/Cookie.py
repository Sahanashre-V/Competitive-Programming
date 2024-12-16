def distributeCookies(cookies, children):
    cookies.sort()  
    children.sort()  
    count = 0
    i = 0  
    j = 0  
    
    while i < len(cookies) and j < len(children):
        if cookies[i] >= children[j]:
            count += 1  
            j += 1 
        i += 1  
    
    return count
