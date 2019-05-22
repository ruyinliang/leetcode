class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        num = 0
        max = 0
        
        for i in s:
            if i not in arr:
                arr.append(i)
            else:
                if (max<len(arr)):
                    max = len(arr)
                for j in arr:
                    num=num+1
                    if (j==i):
                        break
                for k in range(num):
                    if(len(arr)!=0):
                        arr.pop(0)
                num = 0
                arr.append(i)
        if (max > len(arr)):
            return max
        return len(arr)