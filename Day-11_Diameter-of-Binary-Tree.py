"""
Problem statement:
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #I need two functions, first one to calculate the height of the left or right sub-trees
        #second one to calculate the diameter of the tree
        
        return Solution.diameter(root)
        
        
    def height(node):
        if node == None:
            return 0
        else:
            return 1 + max(Solution.height(node.left), Solution.height(node.right)) #recursive
            
    def diameter(root):
        if root == None:
            return 0
        else:
            #Diameter of binary tree is calculated as D = Lheight + Rheight + 1
            #But in our case diameter is not equal the number of nodes in the max height
            #It equal the number of paths in this max height
            #So DNEW = D - 1

            lheight = Solution.height(root.left)
            rheight = Solution.height(root.right)

            #Maybe the heighst path doesn't go through the root node
            #so we will calculate also the right sub-tree diameter 
            #and left sub-tree diameter to test this case

            ldiameter = Solution.diameter(root.left)
            rdiameter = Solution.diameter(root.right)

            return max(lheight + rheight, max(ldiameter,rdiameter))
