# check a string palindrome or not 

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




    