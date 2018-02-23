def connect(root):
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            root = root.next
        root = next
            
