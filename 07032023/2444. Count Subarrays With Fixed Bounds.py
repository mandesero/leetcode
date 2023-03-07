nums = [1] * 9
minK = 1
maxK = 1


def count(arr, minK, maxK):
    if minK == maxK and (n := len(arr)) >= 3:
        return (n + 1) * n // 2
    c = 0
    min_pos = max_pos = -1
    for i, v in enumerate(arr):
        if v == minK:
            min_pos = i
        if v == maxK:
            max_pos = i
        c += min(min_pos, max_pos) + 1
    return c

def countSubarrays(nums, minK, maxK):
    z_i = [-1]
    for i, k in enumerate(nums):
        if k < minK or k > maxK:
            z_i.append(i)

    z_i.append(len(nums) + 1)
    c = 0
    for i in range(len(z_i) - 1):
        c += count(
                nums[z_i[i] + 1: z_i[i + 1]],
                minK,
                maxK
            )
    return c

print(countSubarrays(nums, minK, maxK))          