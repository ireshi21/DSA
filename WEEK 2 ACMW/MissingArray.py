class Solution:
    def repeatedNumber(self, A):
        n = len(A)
        og = [0] * (n + 1)  
        ans = []
        
       
        for num in A:
            if og[num] == 1:  
                ans.append(num)
            og[num] = 1
        
     
        for i in range(1, n + 1):
            if og[i] == 0:
                ans.append(i)
                break
        
        return ans
