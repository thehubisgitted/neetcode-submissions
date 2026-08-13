class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            stored_value = hashmap.get(nums[i])
            if stored_value == None:
                complement = target - nums[i]
                hashmap[complement] = (nums[i], i)

            else:
                return [stored_value[1], i]

        return []
