def deleteNode(root, target):
    if not root:
        return None
    if root.val > target:
        root.right = deleteNode(root.right, target)
    if root.val < target:
        root.right = deleteNode(root.left, target)

    else:
        if not root.right:
            root = root.left
        else:
            root.val = min_val(root.right).min_val
            root.right = deleteNode(root.right, root.val)
    return root

def min_val(root):
    while root.left:
        root = root.left
    return root
