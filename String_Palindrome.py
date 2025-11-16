# check a string palindrome or not 

#A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

#Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Using REGULER EXPRESSION  
import re       # import regular expresion 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=re.sub(r"[^A-Za-z0-9]","",s).lower()   # remove all spaces ,special character and convert to lower case 
                                                  # "[^A-Za-z0-9]" here ^ symbol tell NOT of charecter and number 
        start=0
        end=len(s1)-1
        while start<end:                  # when string is empty the while loop will not run and function automatically return true
            if s1[start]!=s1[end]:
                return False
            start+=1
            end-=1
        return True









# Approach 1 : reverse the string and compare with orginal given string 
def String_palindrome(s):
    rev=s[::-1]
    return rev == s

st="abcba"
ans=String_palindrome(st)
print(ans)



# Approach-2: two pointer approach  , we can not modified a string but access the element using indexing like array 
def check_palindrome(s,i,e):
    while i<=e:
        if s[i] != s[e]:
            return False
        i+=1
        e-=1
    return True

s=input("Enter string:")
e=len(s)-1
ans=check_palindrome(s,0,e)
if ans == True:
    print("String is palindrome")
else:
    print("String is not palindrome")




    