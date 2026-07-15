class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set1={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in set1:
                return [set1[diff],i]
            set1[nums[i]]=i