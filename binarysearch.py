def binary_search(my_list, item):
    ## get the low and high of the list
    ## to keep track of which part of the list you'll search in
    low = 0
    high = len(my_list)-1

    while low <= high:
        ## check the middle element
        mid = (low + high) // 2
        guess = my_list[mid]
        ## if we found the item
        if guess == item:
            return mid
        ## if guess was too high
        if guess > item:
            high = mid - 1
        ## else, guess was too low
        else:
            low = mid + 1
    ## if guess doesn't exist
    return None

my_list = [1,3,5,7,10]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))