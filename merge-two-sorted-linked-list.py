# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l2.val < l1.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l2, l1.next)
            return l1