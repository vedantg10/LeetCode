class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
    # Calculate left sums
        left_sum = [0] * n
        current_left_sum = 0
        for i in range(n):
            left_sum[i] = current_left_sum
            current_left_sum += nums[i]
    
    # Calculate right sums
        right_sum = [0] * n
        current_right_sum = 0
        for i in range(n - 1, -1, -1):
            right_sum[i] = current_right_sum
            current_right_sum += nums[i]
    
    # Calculate absolute differences
        answer = [abs(left_sum[i] - right_sum[i]) for i in range(n)]
    
        return answer