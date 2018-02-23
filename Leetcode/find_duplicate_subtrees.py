from collections import Counter
def find_duplicate(root):
    if not root:
        return []
    cnt = Counter()
    ans = []
    duplicates(root)
    return ans

def duplicates(node):
    if not node:
        return None
    uid = (node.val, duplicates(node.left), duplicates(node.right))
    cnt[uid] += 1
    if counter[uid] == 2:
        ans.append(node)
    return uid
