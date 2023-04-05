def intersection(a, b):
    set = {}
    for i in a:
        set[i] = 0

    intersection = []
    for num in b:
        if num in set:
            intersection.append(num)
    return intersection


# slightly faster but using built in function

# def intersection(a, b):
#   set_a = set(a)
#   return [ item for item in b if item in set_a ]


# brute force solution - may time out in edge case where both lists are same numbers from range(0-5000)
# def intersection(a, b):
#   result = []
#   for item in b:
#     if item in a:
#       result.append(item)
#   return result

print(intersection([4, 2, 1, 6], [3, 6, 9, 2, 10]))  # -> [2,6]
