class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *prev = nullptr;
        ListNode *curr = head;
        while (curr != nullptr) {
            ListNode *nextTemp = curr->next;
            curr->next = prev; // 1 -> None
            prev = curr; // 1, 2, 3, 4
            curr = nextTemp;
        }
        return prev;
    }
};