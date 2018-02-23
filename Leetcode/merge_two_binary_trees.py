def merge_trees(t1,t2):
    if not t1 and not t2:
        return None
    num = 0
    if t1: num += t1.val
    if t2: num += t2.val
    ans = TreeNode(num)
    ans.left = merge_trees(t1 and t1.left,t2 and t2.left)
    ans.right = merge_trees(t1 and t1.right,t2 and t2.right)

    return ans
