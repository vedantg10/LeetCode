class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_s = ""
        for word in s:
            if word.isalnum():
                temp_s += word
        if temp_s.lower() == temp_s[::-1].lower():
            return True
        else:
            return False
        