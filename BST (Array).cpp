#include <iostream>
using namespace std;


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
    void remove(int _data);
    BSTNode *getMax();
    BSTNode *getMin();
    void preorderTraversal();
    void inorderTraversal();
    void postorderTraversal();
private:
    BSTNode *root;
};

BST::BST() {
    this -> root = NULL;
}