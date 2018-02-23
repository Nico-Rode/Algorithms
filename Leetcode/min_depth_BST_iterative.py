def min_depth_BST(root):
    stack = [(root, 1)]
    min_depth = float('inf')
    while stack:
        node, depth = stack.pop()
        if not node.left and not node.right:
            min_depth = min(min_depth, depth)
        if node.left:
            stack.append((node.left, depth+1))
        if node.right:
            stack.append((node.right, depth+1))
    return min_depth
