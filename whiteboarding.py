# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return None.

# You can assume, that the input string has always non-zero length.

# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns None (all the characters are repeated)

# How To Whiteboard
# 1. Read the problem out loud
# 2. Making any assumption, ask claryinging questions. (you are establishing good habits)
# 3. coming up with the approach (drawing pictures) (make sure you dont leave us the viewers in the dust)
# 	- ideally, you can come up with a COUPLE solutions, evaluate their complexities/efficiency/then make your pick
# 4. Write out the code (this should actually take a small amount of time)
# 5. Debug / re-evaluate

def first_non_repeated_char(some_string):

    letters = dict()

    for i in range(len(some_string)):
        if some_string[i] not in letters:
            letters[some_string[i]] = 1
        else:
            letters[some_string[i]] += 1

    
    for i in range(len(some_string)):
        if letters[some_string[i]] == 1:
            return some_string[i]
        else:
            pass
    return None
    
print(first_non_repeated_char('aabbcc'))
