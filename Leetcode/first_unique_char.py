def find_first_unique(string):
    letters = [chr(l) for l in range(ord('a'), ord('z')+1)]
    index = float('inf')
    for l in letters:
        if string.count(l) == 1:
            index = min(index, string.index(l))
    return index if index != float('inf') else -1
