# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def __repr__(self):
        if self.next is None:
            return str(self.val)
        return str(self.val) + " " + str(self.next)


def removeNthFromEnd(head: ListNode, n: int): 
    curr = head
    next = head.next
    i = 0
    while i < n and next != None:
        curr = next
        next = next.next

    # found




nodes = []
prev = None
for i in range(1,5):
    nodes.append(ListNode(i))
    if prev:
        prev.next = nodes[-1]
    prev = nodes[-1]
print(removeNthFromEnd(nodes,2))
        