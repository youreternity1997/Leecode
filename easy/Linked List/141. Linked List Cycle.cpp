// https://leetcode.com/problems/linked-list-cycle/
// Time complexity:0(n)
// Space complexity:0(1)

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL || head->next ==NULL)return false;
        
        ListNode *slow=head;
        ListNode *fast=head;

        while(fast->next){
            fast=fast->next;
            if(fast->next){
                fast=fast->next;
                slow=slow->next;
            }

            if(slow==fast){
                return true;
            }
        }
        return false;
    }
};