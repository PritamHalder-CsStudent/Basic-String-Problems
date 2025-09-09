# Find All String permutation 
# Example : Input -> "abc"-->  Output: "abc", "acb" , "bac", "bca", "cab", "cba"


# Recursive way to solve 
def String_Permutaion(s,left,right):
    if left == right:
       print("".join(s)) 
    else:
        for i in range(left,right+1):
            s[left],s[i]=s[i],s[left]  
            String_Permutaion(s,left+1,right)
            s[left],s[i]=s[i],s[left]


s="abc"
start=0
end=len(s)-1
print(String_Permutaion(list(s),start,end))  # string object does not support item assignment so we pass the string as list 

    
