def compareVersion(v1,v2):
    v1 = [int(v) for v in v1.split('.')]
    v2 = [int(v) for v in v2.split('.')]

    for i in range(max(len(v1),len(v2))):
        num1 = v1[i] if i < len(v1) else 0
        num2 = v2[i] if i < len(v2) else 0
        if num1 < num2: return -1
        if num1 > num2: return 1
    return 0
