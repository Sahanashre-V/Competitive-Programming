def distributeCandies(candies, people):
    result = [0] * people  
    i = 0 
    candy_count = 1  

    while candies > 0:
        result[i] += min(candy_count, candies)  
        candies -= min(candy_count, candies)  
        candy_count += 1  
        i = (i + 1) % people  

    return result
