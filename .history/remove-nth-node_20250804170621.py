# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def __repr__(self):
        if self.next is None:
            return str(self.val)
        return str(self.val) + " " + str(self.next)


def removeNth(head: ListNode, n: int): 
    
    # case its node 1
    if n == 1:
        next = head.next
        return next
    else:

        # Two pointer approach 
        # placed distance between pointer must be of size n 
        temp = None # l - 1
        l = head 
        r = head.next
        d = 1 

        # stops when right pointer goes out of bounds
        while r != None and l:
            # Move right pointer only while d < n
            if d < n:
                r = r.next
            else:
                # Move both pointers
                temp = l
                l = l.next 
                r = r.next
            d += 1
        # Node to delete is at pointer l

        return head



    




nodes = []
prev = None
for i in range(1,5):
    nodes.append(ListNode(i))
    if prev:
        prev.next = nodes[-1]
    prev = nodes[-1]

print(nodes)

print(removeNth(nodes[0],4))
        