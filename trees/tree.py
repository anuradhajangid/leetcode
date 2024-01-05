from collections import deque
from typing import Optional
#https://leetcode.com/problems/invert-binary-tree/description/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree:
    def _createNode(self, value):
        return TreeNode(value)
    
    def insert(self, node:TreeNode, value):
        if node is None:
            return self._createNode(value)
        if value < node.val:
            node.left = self.insert(node.left, value)
        elif value > node.val:
            node.right = self.insert(node.right, value)
        else:
            raise TypeError("Repeated value in tree not allowed")
        return node
    
    def searchBF(self, node: TreeNode, searchvalue):
        if node is None or node.val == searchvalue:
            return node
        
        if searchvalue < node.val:
            return self.search(node.left, searchvalue)
        else:
            return self.search(node.right, searchvalue)
    
    def searchDF(self, node: TreeNode, searchValue):
        queue = []

        if node is None:
            return None
        
        queue.append(node)

        while queue:
            temp = queue.pop()
            if temp.val == searchValue:
                return temp
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)

        
    def delete(self, node, delvalue):
        if node is None:
            return None
        
        if delvalue < node.left:
            self.delete(node.left, delvalue)
        elif delvalue > node.right:
            self.delete(node, node.right)
        else:
            if node.left is None and node.right is None:
                del node
                return None
            else :
                templ = node.left
                tempr = node.right
                del node
                return [templ, tempr]
    
    def traverseInOrder(self, node):
        if node is not None:
            self.traverseInOrder(node.left)
            print(node.value)
            self.traverseInOrder(node.right)

    def traversePreOrder(self, node):
        if node is not None:
            print(node.val)
            self.traversePreOrder(node.left)
            self.traversePreOrder(node.right)
    
    def traversePostOrder(self, node):
        if node is not None:
            self.traversePostOrder(node.left)
            self.traversePostOrder(node.right)
            print(node.val)
    


tr = Tree()
head = None
input = [9,20,15,7]
for item in input:
    head = tr.insert(head, item)