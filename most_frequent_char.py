def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    # {p:1, 0:2, a:1, t:2}

    most_frequent = s[1]
    for i in s:
        # p o t a t o
        if count[i] > count[most_frequent]:
            most_frequent = i
    return most_frequent


print(most_frequent_char('potato'))
