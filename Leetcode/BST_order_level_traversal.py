def order_level_traversal(root):
    if not root:
        return None
    dict = {}
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        if depth in dict:
            dict[depth].append(node.val)
        else:
            dict[depth] = [node.val]
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth +1 ))
    return list(dict.values())
