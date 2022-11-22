class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        #Complete this method
        if head is None:
            return Node(data)
        else:
            current = head
            while current.next is not None:
                current = current.next;
            current.next = Node(data)
            return head




mylist= Solution()
T=[2, 3, 4, 1]
head=None
for i in range(len(T)):
    data=T[i]
    head=mylist.insert(head,data)
mylist.display(head)