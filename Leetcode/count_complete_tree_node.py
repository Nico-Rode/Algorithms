def countleft(root):
    cnt = 0
    while root.left:
        root = root.left
        cnt += 1
    return cnt

def countRight(root):
    cnt = 0
    while root.right:
        root = root.right
        cnt += 1
    return cnt

def countCompleteNodes(root):
    left = countleft(root)
    right = countright(root)
    if left == right:
        return (1<<left)-1
    else:
        return 1 + countCompleteNodes(root.left) + countCompleteNodes(root.right)
