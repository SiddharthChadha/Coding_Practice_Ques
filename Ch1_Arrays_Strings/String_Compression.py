'''
1.6 STRING COMPRESSION

Q1: Is string in ASCII or Unicode format
Q2: Can there be a condition where empty string is passed as input?


Iterate over the string. Create a counter var to keep track of repeated characters. 
After encountering a new character, save the counter value to a new string and reset it. 

Time Complexity: O(n)
Space Complexity: O(n) [Worst case: abcdefghia....]
'''

str1 = 'aabccccccaaa'
str2 = 'aabccccccd'
def string_compression(str1):
    
    counter = 0
    current_char = str1[0]
    result = ''

    for char in str1:

        if char!= current_char: #new character encountered
            result = result + current_char
            result = result + str(counter)
            current_char = char
            counter = 1 
        else:
            counter = counter + 1
    
    result += current_char
    result += str(counter)
    return result

print(string_compression(str1))
print(string_compression(str2))

        