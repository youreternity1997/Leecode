#include <iostream>
using namespace std;
#include <stack>


class BSTNode {
public:
    BSTNode ();
    BSTNode (int _data);
    int data;
    BSTNode *parent, *left, *right;
};

BSTNode::BSTNode() {
    this -> parent = NULL;
    this -> left = NULL;
    this -> right = NULL;
}

BSTNode::BSTNode(int _data) {
    this -> data = _data;
    this -> parent = NULL;
    this -> left = NULL;
    this -> right = NULL;
}

class BST {
public:
    BST();
    void insert(int _data);
    //void insert(BSTNode *, int); // Recursive
    void remove(int _data);
    void preorderTraversal();
    void inorderTraversal();
    void postorderTraversal();
    void levelorder();
    BSTNode *getMax();
    BSTNode *getMax(BSTNode *);
    BSTNode *getMin();
    BSTNode *getMin(BSTNode *);
    BSTNode *search(int);
    BSTNode *search(BSTNode *, int);
    void remove(int);
private:
    BSTNode *root;
};

BST::BST() {
    this -> root = NULL;
}

void BST::insert(int _data)
{
    if (this -> root == NULL)
    {
        this -> root = new BSTNode(_data);
        return;
    }
    else
    {
        BSTNode *cur = this -> root;
        while (true)
        {
            if (cur -> data > _data) // _data <- root -> ~
            {
                if (cur -> left == NULL)
                {
                    cur -> left = new BSTNode(_data);
                    return;
                }
                else
                    cur = cur -> left;
            }
            else // ~ <- root -> _data
            {
                if (cur -> right == NULL)
                {
                    cur -> right = new BSTNode(_data);
                    return;
                }
                else
                    cur = cur -> right;
            }
        }
    }
}

/*
void BST::insert(BSTNode **_root, int _data)
{
    if (this -> root == NULL)
    {
        this -> root = new BSTNode(_data);
        return;
    }

    if (_data > _root -> data) // root -> _data
    {
        if (_root -> right != NULL)
            insert(_root -> right, _data);
        else
        {
            BSTNode *newBSTNode = new BSTNode(_data);
            _root -> right = (newBSTNode); 
            return;
        }
    }
    else // _data <- root
    {
        if (_root -> left != NULL)
            insert(_root -> left, _data);
        else
        {
            BSTNode *newBSTNode = new BSTNode(_data);
            _root -> left = (newBSTNode); 
            return;
        }
    }
}
*/

void BST::preorderTraversal() {
    if (this -> root == NULL) return ;
    BSTNode *cur;
    std::stack <BSTNode *> st;
    st.push(this -> root);
    while (st.size()) {
        cur = st.top();
        st.pop();
        std::cout << cur -> data << " -> ";
        if (cur -> right) st.push(cur -> right);
        if (cur -> left) st.push(cur -> left);
    }
    std::cout << endl;
}

void BST::inorderTraversal() {
    BSTNode *cur = this -> root;
    std::stack <BSTNode *> st;
    while (1) {
        if (cur) {
            st.push(cur);
            cur = cur -> left;
        }
        else {
            if (st.size() == 0) break;
            cur = st.top();
            st.pop();
            cout << cur -> data << " -> ";
            cur = cur -> right;
        }
    }
    std::cout << endl;
}

void BST::postorderTraversal() {
    if (this -> root == NULL) return ;
    BSTNode *cur = this -> root, *temp;
    std::stack <BSTNode *> st;
    while (st.size() || cur) {
        if (cur) {
            st.push(cur);
            cur = cur -> left;
        }
        else {
            temp = st.top() -> right;
            if (temp) {
                cur = temp;
            }
            else {
                temp = st.top();
                st.pop();
                std::cout << temp -> data << " -> ";
                while (st.size() && temp == st.top() -> right) {
                    temp = st.top();
                    st.pop();
                    std::cout << temp -> data << " -> ";
                }
            }
        }
    }
    std::cout << endl;
} 

void BST::levelorder() {
    if (this -> root == NULL) return ;
    std::queue <BSTNode *> q;
    q.push(this -> root);
    while (q.size()) {
        int size = q.size();
        for (int i=0; i<size; i++) {
            std::cout << q.front() -> data << " -> ";
            if (q.front() -> left) q.push(q.front() -> left);
            if (q.front() -> right) q.push(q.front() -> right);
            q.pop();
        }
    }
    std::cout << "end";
}

BSTNode *BST::remove(int target) {
    BSTNode *tg = search(target);
    // 目標節點不存在或二元搜尋樹為空
    if (tg == NULL) {
        std::cout << "NOT FOUND" << std::endl;
        return NULL;
    }
    // 目標節點為樹根
    if (tg == this -> root) { // remove root
        if (tg -> left && tg -> right) { // 2 children
            // tg will be replaced by min of tg -> right
            BSTNode *replaced = getMinPtr(tg -> right);
            if (replaced -> right) {
                if (replaced -> parent -> right == replaced) {
                    replaced -> parent -> right = replaced -> right;
                }
                else {
                    replaced -> parent -> left = replaced -> right;
                }
            }
            if (tg -> right == replaced) {
                replaced -> left = tg -> left;
                tg -> left -> parent = replaced;
            }
            else {
                replaced -> right = tg -> right;
                replaced -> left = tg -> left;
                tg -> right -> parent = replaced -> right;
                tg -> left -> parent = replaced -> left;
            }
            this -> root = replaced;
            return tg;

        }
        else if (tg -> left) { // 1 child : left
            this -> root = tg -> left;
            return tg;
        }
        else if (tg -> right) { // 1 child : right
            this -> root = tg -> right;
            return tg;
        }
        else { // no child
            this -> root = NULL;
            return tg;
        }
    }
    // 目標節點存在，但不為樹根
    else {
        if (tg -> left && tg -> right) { // 2 children
            // tg will be replaced by min of tg -> right
            BSTNode *replaced = getMinPtr(tg -> right);
            if (replaced -> right) {
                if (replaced -> parent -> right == replaced) {
                    replaced -> parent -> right = replaced -> right;
                }
                else {
                    replaced -> parent -> left = replaced -> right;
                }
            }
            replaced -> parent = tg -> parent;
            if (tg -> parent -> right == tg) {
                tg -> parent -> right = replaced;
            }
            else {
                tg -> parent -> left = replaced;
            }
            replaced -> right = tg -> right;
            replaced -> left = tg -> left;
            tg -> right -> parent = replaced -> right;
            tg -> left -> parent = replaced -> left;
            return tg;
        }
        else if (tg -> left) { // 1 child : left
            concat(&(tg -> parent), &tg, &(tg -> left));
            return tg;
        }
        else if (tg -> right) { // 1 child : right
            concat(&(tg -> parent), &tg, &(tg -> right));
            return tg;
        }
        else { // no child
            if (tg -> parent -> left == tg) {
                tg -> parent -> left = NULL;
            }
            else {
                tg -> parent -> right = NULL;
            }
            return tg;
        }

    }

}

// 用來銜接目標節點的父節點與子節點
void concat(Node **tgp, Node **tg, Node **tgc) { 
    if ((*tgp) -> left == *tg) {
        (*tgc) -> parent = (*tgp);
        (*tgp) -> left = (*tgc);
        return ;
    }
    else {
        (*tgc) -> parent = (*tgp);
        (*tgp) -> right = (*tgc);
        return ;
    }
}

BSTNode* BST::LCA(BSTNode *root, BSTNode *tg1, BSTNode *tg2) {
        if (root == NULL) return NULL;
        if (tg1 == root || tg2 == root) 
            return root;
        if ((root -> data > tg1 -> data && root -> data < tg2 -> data) || (root -> data < tg1 -> data && root -> data > tg2 -> data)) 
            return root;
        else if (root -> data > tg1 -> data && root -> data > tg2 -> data) 
            return lowestCommonAncestor(root -> left, tg1, tg2);
        else 
            return lowestCommonAncestor(root -> right, tg1, tg2);
}

void inorderTraversal(std::vector<int> *temp, BSTNode *root) {
    if (root == NULL) return ;
    if (root -> left) inorderTraversal(temp, root -> left);
    temp -> push_back(root -> data);
    if (root -> right) inorderTraversal(temp, root -> right);
}
bool BST::isValid() {
    std::vector<int> temp;
    inorderTraversal(&temp, this -> root);
    int prev = INT_MIN;
    for (int i: temp) {
        if (i <= prev) return false;
        prev = i;
    }
    return true;
}

int main() {
    BST *bst = new  BST;
    bst -> insert(1);
    bst -> insert(2);
    bst -> insert(3);
    bst -> insert(4);
    bst -> insert(5);
    bst -> insert(6);
    bst -> insert(7);
    bst -> insert(8);

    bst -> preorderTraversal();

    bst -> inorderTraversal();
    bst -> postorderTraversal();
    //dll -> printAll();
    return 0;
}



