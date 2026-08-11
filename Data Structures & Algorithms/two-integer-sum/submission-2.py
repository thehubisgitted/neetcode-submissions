class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
          remainder_exists = hashmap.get(nums[i])
          if remainder_exists == None:
            remainder = target - nums[i]
            hashmap[remainder] = (nums[i], i)
          else:
            return [remainder_exists[1], i]
          
        return []
        #First check if there is a compliment
        #7 -3 = 4
        #save in case there is a compliment later
        #[4] = 3

        