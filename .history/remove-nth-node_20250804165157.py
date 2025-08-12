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

        # Return the original head
        # Assume node to del is node 2
        nodeToDel = head.next
        # Dont change node to del until we traversed n nodes
        cnt = 2 
        # Skip to nth node
        ptr1_prev = None
        ptr1 = head
        ptr2 = nodeToDel
        while ptr1 and ptr2:
            cnt += 1

            # reached nth term
            if cnt >= n:
                # move ptr1 if ptr2 can go forward
                if ptr2.next:
                    ptr1 = ptr1.next

            ptr2 = ptr2.next


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
        