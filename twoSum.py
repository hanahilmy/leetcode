class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = []; 
        i=0
        while i<len(nums): 
            j=i+1
            while j<len(nums):
                if nums[i]+nums[j]==target:
                    results.append(i)
                    results.append(j)
                    return results
                j=j+1
            i=i+1

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  
print(solution.twoSum([3, 2, 4], 6))       
print(solution.twoSum([3, 3], 6))          
        
