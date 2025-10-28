# Problem 
# Given two strings s1 and s2. Return true if the string s2 can be obtained by rotating (in any direction) string s1 by exactly 2 places, otherwise, false.

# Note: Both rotations should be performed in same direction chosen initially.

# Examples:

# Input: s1 = "amazon", s2 = "azonam"
# Output: true
# Explanation: "amazon" can be rotated anti-clockwise by two places, which will make it as "azonam".

# Input: s1 = "geeksforgeeks", s2 = "geeksgeeksfor"
# Output: false
# Explanation: If we rotate "geeksforgeeks" by two place in any direction, we won't get "geeksgeeksfor".

# Input: s1 = "ab", s2 = "ab"
# Output: true
# Explanation: If we rotate "ab" by two place in any direction, we always get "ab".


# Using string slicing method we can rotate the array 

def isRotated(s1,s2):
    if len(s1)!=len(s2):
        return False
    if len(s1)==2 and s1==s2: # when two given string are same and length are equal
        return True
            
    # using string slicing we rotate the string 
        
    d=2 # number of position to rotate
        
    # left rotate --clockwise
    
    part1=s1[:d] # first d charecter
    part2=s1[d:] # remaining part 
    left_rotate=part2+part1
        
    # right rotation--anti clock
        
    part3=s1[-d:] # last d charecter 
    part4=s1[:-d] # reaming part 
    right_rotate=part3+part4
        
    if left_rotate==s2 or right_rotate==s2:
        return True
    return False


print(isRotated("amazon","azonam"))