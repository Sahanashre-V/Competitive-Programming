class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        s={}
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                s[arr[i]/arr[j]] = [arr[i],arr[j]]
        n=sorted(s.keys())
        small=n[k-1]
        return s[small]