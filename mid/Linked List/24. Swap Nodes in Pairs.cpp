/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode *prenode;
        ListNode *n1,*n2;
      if(head == nullptr || head->next == nullptr)
          return head;
      ListNode *node = new ListNode();
      node->next = head;
      prenode = node;
      n1 = prenode->next;
      n2 = n1->next;
      while( n1 != nullptr && n2 != nullptr){
          prenode->next = n2;
          n1->next = n2->next;
          n2->next = n1;
          prenode = n1;
          n1 = prenode->next;
          if(n1 != nullptr && n1->next != nullptr)
              n2 = n1->next;
          else
            break;
      }
        return node->next;        
    }
};