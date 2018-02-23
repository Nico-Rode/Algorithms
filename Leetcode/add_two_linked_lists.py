def add_two_lists(node1,node2):
    n = ListNode(0)
    carry = 0
    root = n
    while node1 or node2 or carry:
        v1,v2 = 0,0
        if node1:
            v1 = node1.val
            node1 = node1.next
        if node2:
            v2 = node2.val
            node2 = node2.next
        carry, result = divmod(v1+v2+carry, 10)
        n.next = ListNode(result)
        n = n.next
    return root.next
