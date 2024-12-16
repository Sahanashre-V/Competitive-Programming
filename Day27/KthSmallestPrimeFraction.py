def kthSmallestPrimeFraction(A, K):
    def countLessThan(target):
        count, j = 0, len(A) - 1
        for i in range(len(A)):
            while j > i and A[i] / A[j] > target:
                j -= 1
            count += j - i
        return count

    left, right = 0, 1  
    while left < right:
        mid = (left + right) / 2
        if countLessThan(mid) < K:
            left = mid
        else:
            right = mid
    return [A[i], A[j]]

