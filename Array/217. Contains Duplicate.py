class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for num in nums:
            if num not in temp:
                temp.add(num)
            else:
                return True
        return False
        