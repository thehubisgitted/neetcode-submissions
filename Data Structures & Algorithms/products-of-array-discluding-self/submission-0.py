class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        answer = []
        for i in range(len(nums)):
            if i == 0:
                pre[0] = 1
            else:
                value = nums[i-1] * pre[i-1]
                pre[i] = value
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                post[i] = 1
            else:
                value = nums[i+1] * post[i+1]
                post[i] = value
        
        for i in range(len(nums)):
            answer.append(post[i]*pre[i])
        return answer