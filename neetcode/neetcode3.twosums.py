class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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