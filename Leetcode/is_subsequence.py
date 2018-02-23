def is_subsequence(s1, s2):
    if not s1:
        return True
    i, p = 0,0
    current = s1[0]
    while i < len(s2):
        if current = s2[i]:
            p+=1
            if p == len(s1):
                return True
            current = s1[p]
        i+=1
    return False
