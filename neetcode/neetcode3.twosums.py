
class Solution:
    def twoSum(self, nums, target):
        i=0;
        k=0;
        while i <(len(nums)):
            while k<(len(nums)):
                if k !=i:
                    self=nums[i]+nums[k];
                    if self==target:
                        return [i,k]
                k=k+1;
            i=i+1;
            k=0;
nums=[1,2,3,4,5,6]
target=6
solution=Solution()
print(solution.twoSum(nums,target))  # Output: True