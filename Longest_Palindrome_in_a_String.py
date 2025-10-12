# Given a string s, your task is to find the longest palindromic substring within s.

# Example 1

''' Input: s = “forgeeksskeegfor” 
Output: “geeksskeeg”
Explanation: There are several possible palindromic substrings like “kssk”, “ss”, 
“eeksskee” etc. But the substring “geeksskeeg” is the longest among all. '''
 
# Example 2

''' Input: s = “Geeks” 
Output: “ee”
Explanation: "ee" is the longest palindromic substring of "Geeks". ''' 

# Approach:
# 1.  Generate all possible substrings of the given string. 
# 2 .  For each substring, check if it is a palindrome.
#       If it is, 
        # update the result if its length is greater than the longest palindrome found so far.
        
def check_palindrome(s,start,end):
    while start<end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True


def longest_pailndrome_subString(s):
    n=len(s)
    maxLen=1
    start=0
    for i in range(0,n):
        for j in range(i,n):
            if check_palindrome(s,i,j) and (j-i+1)>maxLen:   #  check if the current substring is a palindrome
                start=i
                maxLen=j-i+1
    return s[start:start+maxLen]      


print(longest_pailndrome_subString("forgeeksskeegfo"))      
            
    

