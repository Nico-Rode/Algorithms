def find_two_sum(root,target,ans):
    if not root:
        return False
    if root.val in set:
        return True
    ans.add(target-root.val)
    return find_two_sum(root.left,target,ans) or find_two_sum(root.right,target,ans)
