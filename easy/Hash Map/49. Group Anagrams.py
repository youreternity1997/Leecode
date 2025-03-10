# https://leetcode.com/problems/group-anagrams/solutions/4683832/beats-99-users-c-java-python-javascript-2-approaches-explained/
# Time complexity: O(n∗k∗logk) (K is the length of the longest string)
# Space complexity: O(n∗k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        ans = []

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in mp:
                ans[mp[sorted_str]].append(s)
            else:
                mp[sorted_str] = len(ans)
                ans.append([s])
                
        return ans
