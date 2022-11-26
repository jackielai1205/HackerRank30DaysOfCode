class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        duplicated_list = []
        current = head
        duplicated_list.append(current.data)
        while current.next is not None:
            if current.next.data not in duplicated_list:
                duplicated_list.append(current.next.data)
                current = current.next
            else:
                current.next = current.next.next
        return head


mylist= Solution()
T= 6
head=None
test = [1, 2, 2, 3, 3, 4]
for i in range(T):
    data=test[i]
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head)