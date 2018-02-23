def LCA(root,l1,l2):
    if not root:
        return None
    while True:
        if l1.val > root.val and l2.val > root.val:
            root = root.right
        elif l1.val < root.val and l2.val < root.val:
            root = root.right
        else:
            return root
