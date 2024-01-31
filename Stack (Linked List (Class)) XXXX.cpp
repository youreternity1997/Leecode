// 將鏈結串列的 head 設為私有變數，以確保外人無法觸及
// 想要取得堆疊中的資料，唯有透過 getTop()
class Stack
{
private:
    SLLNode *head;
public:
    Stack();
    bool isEmpty();
    void push(int); 
    int pop(); 
    int getTop();
};

Stack::Stack() { this -> head = NULL; }

bool Stack::isEmpty() { return this -> head == NULL; }

void Stack::push(int _data) {
    if (this -> head == NULL)
    {
        this -> head = new SLLNode(_data);
        this -> head -> next = NULL;
    }
    else 
    {
        SLLNode *cur = this -> head;
        while (cur && cur -> next != NULL) 
        {
            cur = cur -> next;
        }
        cur -> next = new SLLNode(_data);
    }
}

int Stack::pop() {
    if (head == NULL) 
        return -1;
    int toBeReturn;
    if (head -> next == NULL)
    {
        toBeReturn = head -> data;
        delete head;
        head = NULL;
    }
    else
    {
        SLLNode *cur = head;
        SLLNode *prev;
        while (cur && cur -> next != NULL)
        {
            prev = cur;
            cur = cur -> next;
        }
        toBeReturn = cur -> data;
        delete cur;
        prev -> next = NULL;
    }
    return toBeReturn;
}