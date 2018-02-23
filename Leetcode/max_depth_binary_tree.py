#Beats 100% of all other users

def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right))+1
