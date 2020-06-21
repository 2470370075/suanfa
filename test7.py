l1 = [2,4,6,8,9,999]
l2 = [1,3,4,44,99]

def merge(l1,l2):
    l3 = []
    i,j = 0,0
    while i < len(l1) and j < len(l2):
        if l1[i]>l2[j]:
            l3.append(l2[j])
            j += 1
        else:
            l3.append(l1[i])
            i += 1
    if j == len(l2):
        l3 += l1[i:]
    if i == len(l1):
        l3 += l2[j:]
    return l3
print(merge(l1,l2))
