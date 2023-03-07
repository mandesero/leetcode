from collections import defaultdict


def csort(arr):
    tmp = defaultdict(int)
    min_v, max_v = min(arr), max(arr)
    for elem in arr:
        tmp[elem] += 1

    j = 0
    for i in range(min_v, max_v + 1):
        while tmp[i] > 0:
            arr[j] = i
            tmp[i] -= 1
            j += 1
    return arr    


arr = [5,1,1,2,0,0]

res = csort(arr)
print(res)