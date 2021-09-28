class Solution:  
    def compute(self, arr):
        product=1
        for a in arr:
            product*=a
        return product
   
    def trimFirstNeg(self, arr):
        tmp=[]
        encounter=False;
        for a in arr:
            if False==encounter:    
                if a < 0:
                    encounter=True
            else:
                tmp.append(a)
        return tmp if len(tmp)>0 else [0]
                
    def conquer(self, arr, negCounter):
        if 0==negCounter%2:
            return self.compute(arr)
        else:
            case1=self.trimFirstNeg(arr)
            case2=self.trimFirstNeg(arr[::-1])
            return max(self.compute(case1), self.compute(case2))

    def divide(self, nums):
        subarray=[]
        negCounter=0
        tmp=[]
        for a in nums:
            if a < 0:
                negCounter+=1
                tmp.append(a)
            elif a > 0:
                tmp.append(a)
            else:
                subarray.append((tmp,negCounter))
                negCounter=0
                tmp=[]
        return subarray
            
    def maxProduct(self, nums):
        if 1==len(nums):
            return nums[0]
        nums.append(0)
        subarray = self.divide(nums)
        maxProduct=0
        for sa in subarray:
            if len(sa[0])>0:
                result=self.conquer(sa[0],sa[1])
                if result > maxProduct:
                    maxProduct=result
        return maxProduct

sln=Solution()
assert 6==sln.maxProduct(nums = [2,3,-2,4])
assert 0==sln.maxProduct(nums = [-2,0,-1])
assert 31850496==sln.maxProduct(nums = [2,3,-2,4,2,3,-2,4,2,3,-2,4,2,3,-2,4,2,3,-2,4])
assert 55296==sln.maxProduct(nums = [2,3,4,2,3,-2,4,2,3,-2,4])
assert 2==sln.maxProduct(nums = [2])
assert -2==sln.maxProduct(nums = [-2])
                
                
                
                
                
        
        
        