def buildTree(inorder, preorder):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder.pop(0))
    inorder_index = inorder.index(root.val)
    root.left = buildTree(inorder[:index], preorder)
    root.right = buildTree(inorder[inorder_index+1:], preorder)

    return root
