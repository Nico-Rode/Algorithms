def find_kth_smallest_node(root, k):
    ans = []
    ans = in_order_traversal(root, ans)
    return ans[k-1]



def in_order_traversal(root, ans):
    if not root:
        return None
    in_order_traversal(root.left)
    ans.append(root.val)
    in_order_traversal(root.right)
    return ans
