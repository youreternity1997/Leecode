class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        minimum, maximum= min(strs), max(strs)
        for i in range(len(minimum)):
            if minimum[i] != maximum[i]: 
                break
            else: ans+=minimum[i]
        return ans


strs = ["ad", "a"]
ans = Solution().longestCommonPrefix(strs)
print(ans)