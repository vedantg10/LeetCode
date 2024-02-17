class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        output = []
        output.append(pref[0])
        for i in range(1,len(pref)):
            output.append(pref[i] ^ pref[i-1])
        return output