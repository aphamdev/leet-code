def compress(s):
    # add a special character to the string since prompt says s will be alphabetical
    s += "!"
    # initiate two pointer variables
    i = 0
    j = 0
      # initiate empty list
    results = []

      #while our second pointer is less than the the length of s
    while j < len(s):
    # if s[j] is pointing to the same letter as s[i]
      if s[i] == s[j]:
    # j += 1
        j += 1
    # else (once j is pointing to a letter that isn't the same as i):
      else:
      # initiate a number variable to be the difference of j - i
        number = j - i
        # we have to check if there is only one letter, we don't want it to show up as "1t", we just want it to show the letter
        if number == 1:
          results.append(s[i])
        else:
      # add the result of the number and the letter to the list
          results.append(str(number) + s[i])
        # catch up i pointer to j
        i=j


    # "".join(result)
    return ''.join(results)






print(compress('ccaaatsss'))
