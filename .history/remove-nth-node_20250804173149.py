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

    # Two pointer approach 
    # placed distance between pointer must be of size n 
    temp = None # l - 1
    l = head 
    r = head.next
    d = 1 

    # case [1]
    if r == None:
        return None
    # case [1,2]
    if r.next == None:
        if n == 2:
            head.next = None
            return head
        if n == 1:
            return head.next

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

    # Node to delete is at pointer l # Delete (set l-1 to r)
    if temp:
        temp.next = r
    elif l:
        # there was no previous
        return l.next # new head

    # return original head
    return head



    




nodes = []
prev = None
for i in range(1,5):
    nodes.append(ListNode(i))
    if prev:
        prev.next = nodes[-1]
    prev = nodes[-1]

print(nodes)

print(removeNth(nodes[0],2))
        