chars = ["a","b","b","c","c","c"]

def compress(s) -> int:
    if len(s) == 1:
        return 1

    res = 0
    i, j = 0, 0
    while i < len(s):
        char = s[i]
        count = 1
        i += 1
        while i < len(s) and s[i] == char:
            count += 1
            i += 1
        res += 1 + len(str(count)) if count != 1 else 1
        
        s[j] = char
        j += 1

        if count > 1:
            for c in str(count):
                s[j] = c
                j += 1
    
    return res

print(compress(chars))
print(chars)
        
