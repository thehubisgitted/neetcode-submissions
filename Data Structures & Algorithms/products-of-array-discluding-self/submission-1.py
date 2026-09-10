class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        i = 0
        # 1 2 4 6
        # 1 1 1 1
        product = 1
        while i < len(nums):
            answer[i] = product
            product *= nums[i]
            i+=1

        secondproduct = 1
        j = len(nums) - 1
        while j > -1:
            answer[j] *= secondproduct
            secondproduct *= nums[j]
            j-=1
        return answer

