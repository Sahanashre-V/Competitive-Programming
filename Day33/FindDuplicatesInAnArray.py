def findDuplicates(arr):
    seen = set()
    duplicates = []
    
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    
    return duplicates
