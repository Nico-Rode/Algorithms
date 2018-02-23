def find_two_sum(root, target):
    if not root:
        return False
    ans = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val in ans:
            return (node.val, target - nod.val)
        else:
            ans.append(target - node.val)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return False
    
