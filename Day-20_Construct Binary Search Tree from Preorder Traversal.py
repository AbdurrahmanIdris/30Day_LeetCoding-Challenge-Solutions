"""
Problem statement:
Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.
left has a value < node.val, and any descendant of node.right has a value > node.val.  
Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 
1 <= preorder.length <= 100
The values of preorder are distinct.
"""
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def insert(self,x):
        if self.val:
            if x < self.val:
                if self.left == None:
                    self.left = TreeNode(x)
                else:
                    self.left.insert(x)
            if x > self.val:
                if self.right == None:
                    self.right = TreeNode(x)
                else:
                    self.right.insert(x)
        else:
            self.val = x

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        tree = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            tree.insert(preorder[i])
        return tree
