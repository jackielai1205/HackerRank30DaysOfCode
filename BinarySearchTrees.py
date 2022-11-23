class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        left_height = 0
        right_height = 0
        if root.left is not None:
            left_height = self.getHeight(root.left) + 1
        if root.right is not None:
            right_height = self.getHeight(root.right) + 1
        if left_height > right_height:
            return left_height
        else:
            return right_height



T = 7
myTree = Solution()
root = None
arr = [3, 5, 2, 1, 4, 6, 7]
for i in range(T):
    data=arr[i]
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)