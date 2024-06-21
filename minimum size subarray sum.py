class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        curr_sum = 0
        l, ans = 0, float("inf")

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                ans = min(ans, r-l+1)
                curr_sum -= nums[l]
                l += 1
        
        return 0 if ans == float("inf") else ans