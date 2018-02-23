def trimBST(root, lower, upper):
    if not root:
        return None
    if root.val < lower:
        return trimBST(root.right, lower, upper)
    if root.val > upper:
        return trimBST(root.left, lower, upper)
    root.right = trimBST(root.right, lower, upper)
    root.left = trimBST(root.left, lower, upper)
    return root
