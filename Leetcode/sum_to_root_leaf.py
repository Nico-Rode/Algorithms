def sum_root_to_leaf(root):
    if not root:
        return 0
    return in_order_traversal(root, 0)

def in_order_traversal(root, total):
    if not node:
        return 0
    total = (total*10) + root.val
    if not root.left and not root.right:
        return total
    return in_order_traversal(root.left, total) + in_order_traversal(root.right, total)
