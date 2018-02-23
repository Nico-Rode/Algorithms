def LCA(root, l1, l2):
    if not root:
        return None
    parents = {root:None}
    stack = [root]
    while l1 not in parents or l2 not in parents:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
            parents[node.left] = node
        if node.right:
            stack.append(node.right)
            parents[node.right] = node
    ancestors = set()
    while l1:
        ancestors.add(l1)
        l1 = parents[l1]
    while l2 not in ancestors:
        l2 = parents[l2]

    return l2
