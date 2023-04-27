# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups
# according to the following pattern:
# <number><char>
# for example, '2c' or '3a'

# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively.
# You may assume that the input string is well-formed according to the previously mentioned pattern.
#
# uncompress("2c3a1t") # -> 'ccaaat'


def uncompress(s):
    # set numbers so we can check if j is a number
    numbers = "0123456789"
    # create a list since it'll have better time complexity than
    # adding and copying a string
    results = []
    # initialize our variables
    i = 0
    j = 0
    # start our while loop
    while j < len(s):
        # check if s[j] is a numeric value
        if s[j] in numbers:
            # we want to increase j by 1 if it is - again we looking for
            #  the alphanumeric char
            j += 1
        else:
            # initialize a new variable num and we want to get the numeric
            #  value of the nums so int( ) using string splice
            num = int(s[i:j])
            results.append(s[j] * num)
            j += 1
            i = j
    return ''.join(results)


print(uncompress('2t3o11g2s'))
