def pair_product(numbers, target_product):
    # create a hash map
    previous_nums = {}

    # loop through list of numbers using enumerate which will get us the index and numbers
    for index, num in enumerate(numbers):
        # # find the multiple of target_product
        multiple = target_product / num
        # if multiple is in hash map,
        if multiple in previous_nums:
            # return index of both those numbers
            return index, previous_nums[multiple]

        # we have to initialize what the key value in our hash map is we
        previous_nums[num] = index


print(pair_product([3, 2, 5, 4, 1], 8))  # -> (1, 3)
