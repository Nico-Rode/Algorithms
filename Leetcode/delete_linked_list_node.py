def deleteNode(node):
    next = node.next
    node.val = next.val
    node.next = next.next
