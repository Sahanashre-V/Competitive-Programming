def restoreIpAddresses(s):
    def is_valid(segment):
        return 0 <= int(segment) <= 255 and (segment == "0" or segment[0] != "0")

    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s): 
                result.append(".".join(path))
            return

        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            if is_valid(segment):
                backtrack(end, path + [segment])

    result = []
    if len(s) >= 4 and len(s) <= 12: 
        backtrack(0, [])
    return result
