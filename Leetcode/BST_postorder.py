#postorder -> LRV

def iterative_postorder_traversal(root):
    stack = [root]
    path = []
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        path.append(root.val)
    return path.reverse()





def recursive_postorder_traversal(root, ans = []):
    if not root:
        return None
    recursive_postorder_traversal(root.left, ans)
    recursive_postorder_traversal(root.right, ans)
    ans.append(root.val)
    return ans
