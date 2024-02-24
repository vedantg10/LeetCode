class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr =[]
        nums.sort(reverse=True)
        n = len(nums)
        i=0
        while i<n:
            a = nums.pop()
            b = nums.pop()
            arr.append(b)
            arr.append(a)
            i +=2
        return arr
            
            