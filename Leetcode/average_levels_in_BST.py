def averageOfLevels(root):
    ans = [0]
    current_depth = 0
    total = 0
    queue = [(root,0)]
    count = 0
    for node, depth in queue:
        if depth != current_depth:
            current_depth = depth
            total, count = 0,0
            ans.append(0)
        total += node.val
        ccount += 1
        ans[depth] = (total/count)

        if root.left: queue.append((root.left, depth+1))
        if root.right: queue.append((root.right, depth+1))
    return ans
