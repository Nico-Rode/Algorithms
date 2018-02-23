def traverse_tree(root):
    if not root:
        return 0
    return max_path(root, float('-inf'))

def max_path(root, max_path):
    if not root:
        return 0
    left = max(0, max_path(root.left))
    right = max(0, max_path(root.right))
    max_path = max(max_path, left+right+root.val)
    return (max(left,right) + root.val)
