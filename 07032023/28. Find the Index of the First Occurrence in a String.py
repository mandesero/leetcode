haystack = "sadbutsad"
needle = "sad"


def find_ins(haystack, needle):
    i = 0
    n = len(needle)
    m = len(haystack)
    if n == m and haystack == needle:
        return 0
    for i in range(m - n + 1):
        if haystack[i: i + n] == needle:
            return i
    return -1




# print(find_ins(haystack, needle))
print(find_ins("abc", "c"))