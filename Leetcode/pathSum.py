def hasPathSum(root, k, total = 0):
    if not root:
        return False
    total += root.val
    if not root.left and not root.right and total == k:
        return true
    return hasPathSum(root.left, k, total) or hasPathSum(root.right, k, total)
