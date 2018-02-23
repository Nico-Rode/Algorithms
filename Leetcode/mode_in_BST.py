def find_mode(root):
    current_depth, total, cnt = 0,0,0
    stack = [(root,0)]
    avgs = [0]
    while stack:
        node, depth = stack.pop()
        if depth != current_depth:
            current_depth = depth
            total = 0
            cnt = 0
            avgs.append(0)
        cnt += 1
        total += node.val
        avgs[depth] = (total/cnt)
        if node.left: stack.append((node.left, depth+1))
        if node.right: stack.append((node.right, depth+1)
    return avgs
