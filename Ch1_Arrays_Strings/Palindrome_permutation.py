'''

PALINDROME PERMUTATION

Write a func to check if a string is a permutation of a palindrome?

I: Tact Coa
O: True( permutations: “taco cat”, “acto cta”)

SOLN.

Clarifying Ques:
    Are string char ASCII or Unicode
    Can there be alphanumeric strings
    Will there be a space in between the input string?
    Can I assume everything is in lower case

Method1:

    Iterate over every char in the string and find their frequencies (# times a char appears in the string).
    Save char and their respective frequency as key value pairs in hashmap.
    If all frequencies except one are multiples of 2, then it’s possible to make a palindrome eg: XYZGZYX

    Time Complexity: O(n)
    Space Complexity: O(1) (only 26 key value pairs. Not a function of number of char in strings)


Method 2:

    Time Complexity: O(n)
    Space Complexity: O(1)
    Use a bit vector to save more space

'''
#Method1
def IsPalindromePermutation(str):
  str = str.lower()
  if(len(str) == 0 or len(str) == 1):
    return True

  map = {}

  for char in str:
    if(char == ' '):
      continue
    if(char in map.keys()):
      map[char] = map[char] + 1
    else:
      map[char] = 1
  flag = 0

  for key in map.keys():
    if(map[key] % 2 == 1):
      flag = flag + 1

  if(flag != 1):
    return False
  return True

print(IsPalindromePermutation("tact coa")) #True
print(IsPalindromePermutation("elllehoh")) #False
