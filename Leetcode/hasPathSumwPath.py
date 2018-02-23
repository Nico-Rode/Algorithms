def hasPathSum(root, target):
    path, ans = [], []
    find_paths(root, target, path, ans)
    return ans

def find_paths(root, target, path, ans):
    if not root:
        return None
    total += root.val
    if not root.left and not root.right and total == target:
        ans.append([root.val] + path)
    path.append(root.val)
    find_paths(root.left, target, path, ans)
    find_paths(root.right, target, path, ans)
    path.pop()
