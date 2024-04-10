// Time : O(2N+N)
// Space : O(N)

class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> arr = new HashSet<>();
        for (int num : nums) {
            arr.add(num);
        }
        
        int maxx = 0;
        
        for (int i : nums) {
            int x = i - 1;
            int curr = 0;
            
            if (!arr.contains(x)) {
                while (arr.contains(x + 1)) {
                    curr += 1;
                    x += 1;
                }
                
                maxx = Math.max(maxx, curr);
            }
        }
        
        return maxx;
    }
}