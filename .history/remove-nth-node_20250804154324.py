# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __str__(self):
        return str(self.val)


def removeNthFromEnd(head: list[ListNode], n: int): 
    res : list[ListNode] = []
    print(head)

    return res

nodes = []
prev = None
for i in range(1,5):
    nodes.append(ListNode(i))
    if prev:
        prev.next = nodes[-1]
    prev = nodes[-1]
print(removeNthFromEnd(nodes,2))
        