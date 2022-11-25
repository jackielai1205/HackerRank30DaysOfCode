import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        queue = []
        if root is not None:
            self.level_order_helper(root, queue, "")

    def level_order_helper(self, node, queue, output):
        output += str(node.data) + " "
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        if len(queue) > 0:
            self.level_order_helper(queue.pop(0), queue, output)
        else:
            print(output)


T = 6
myTree = Solution()
root = None
test = [3, 5, 4, 7, 2, 1]
for i in range(T):
    data = test[i]
    root = myTree.insert(root, data)
myTree.levelOrder(root)
