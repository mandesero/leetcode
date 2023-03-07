def jump(arr, cur_ind, count):
    if cur_ind == len(arr) - 1:
        return count
    
    if count >= len(arr):
        return len(arr) + 1

    t1 = t2 = t3 = len(arr) + 1
    t1 = min([jump(arr, j, count + 1) for j in range(len(arr)) if (arr[cur_ind] == arr[j] and cur_ind != j)], default=len(arr) + 1)
    if cur_ind < len(arr):
        t2 = jump(arr, cur_ind + 1, count + 1)
    if cur_ind >= 1:
        t3 = jump(arr, cur_ind - 1, count + 1)
    return min(t1, t2, t3)

def minJump(arr):
    arr = [11,22,7,7,7,7,7,7,7,22,13]
    
    print(jump(arr, 0, 0))


minJump([])