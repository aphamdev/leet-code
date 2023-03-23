def compress(s):
    s += "!"
    results = []
    i = 0
    j = 0
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                results.append(s[i])
            else:
                results.append(str(num) + s[i])

            i = j
    return ''.join(results)


print(compress('ccaaatsss'))
