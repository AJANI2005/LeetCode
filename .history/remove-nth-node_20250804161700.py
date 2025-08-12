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
    
    # case its node 1
    if n == 1:
        next = head.next
        return next
    else:
        prev = None
        curr = head
        next = head.next
        i = 1 
        while i != n and next:
            i+=1
            prev = curr
            curr = next
            next = curr.next
        # at the node to delete
        if(prev): prev.next = next
        curr.next = None
        # Return the original head
        return head



    




nodes = []
prev = None
for i in range(1,5):
    nodes.append(ListNode(i))
    if prev:
        prev.next = nodes[-1]
    prev = nodes[-1]

print(nodes)

print(removeNthFromEnd(nodes[0],4))
        