def min_depth_BST(root,depth=1):
    if not root:
        return 0
    if not root.left and not root.right:
        return depth
    if not root.left:
        return min_depth_BST(root.right, depth + 1)
    if not root.right:
        return min_depth_BST(root.left, depth + 1)
    return min(min_depth_BST(root.left, depth+1), min_depth_BST(root.right, depth + 1))
