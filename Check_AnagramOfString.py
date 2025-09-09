# Check anagram of given two string 
# An anagram of a string is formed by rearranging its letters to make another word or phrase, 
# using all the orginal letters exactly once 
# Example : listen --> silent, 
#           race--> care,acre  


def are_anagram(s1,s2):
    return sorted(s1) == sorted(s2)

ans=are_anagram("listen","silent")
print(ans)