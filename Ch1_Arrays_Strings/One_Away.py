
'''
1.5 One away:
    3 types of edit on string: add char, remove char or replace
    Given 2 strings write a func to check if they are one edit or (zero edits) away

Clarifying ques
    Q1: String be ASCII or Unicode
    Q2: Can I expect strings to just contain alphabets
    Q3: Can I assume all lower case

Method:
    loop through 1st string. Populate the character tracker array.  
    Loop through 2nd string, decrease the count of character stored inside tracker array for every character

    If tracker array contains only single 1 (rest are zeros): One edit away
    If tracker array contains 2 locations as 1, this means that a character was replaced: One edit away
    If tracker array contains all zeroes: No edit away

    If tracker array contains '1' at more than 2 locations then it is more than one edit
  
Time Complexity: O(n)
Space Complexity: O(1) because it's a constant function as it does not depend on size of either string
'''

def one_away(str1, str2):

    char_tracker = []
    loc = 0
    no_of_ones = 0

    for i in range(26):
        char_tracker.append(0)

    for char in str1:
        loc = ord(char) - ord('a') 
        if char_tracker[loc] > 0:
            char_tracker[loc] += 1
        else:
            char_tracker[loc] = 1

    for char in str2:
        loc = ord(char) - ord('a') 
        if char_tracker[loc] > 0:
            char_tracker[loc] -= 1
        else:
            char_tracker[loc] = 1

    for element in char_tracker:
        if(element == 1):
            no_of_ones += 1
    
    if(no_of_ones == 1 or no_of_ones == 2 or no_of_ones == 0):
        return True
    else:
        return False

print(one_away('pale', 'ple'))
print(one_away('pales', 'pale'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bake'))




