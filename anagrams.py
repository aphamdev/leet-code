def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)
# then we'll run this comparison to check if the hash maps are the same

#we'll use a helper function, char count to iterate through the first string and place it in a hash map
def char_count(s):
  count = {}

  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1

  return count
