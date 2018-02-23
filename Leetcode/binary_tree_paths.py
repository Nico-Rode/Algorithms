def find_paths(root):
    if not root:
        return []
    paths, results = [], []
    traverse_tree(root, paths, results)
    return results

def traverse_tree(root, paths, results):
    if not root.left and not root.right:
        results.append([root.val] + paths)
    paths.append(root.val)
    if root.left:
        traverse_tree(root.left, paths, results)
    if root.right:
        traverse_tree(root.right, paths, results)
    paths.pop()
    return paths
