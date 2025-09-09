# String Length encoding - consicutive characters are compressed 
# Example : "aaabbc" -> a3b2c1
#            "abcabc"->a1b1c1a1b1c1


def String_RLE(s):
    if s =="":        # base case empty string return empty string 
        return ""
    res=" "
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:   # compaire the string to count num of occurence 
            count+=1
        else:
            res=res+s[i-1]+str(count)   # if duplicate element no match , then it added result and set count =1 
            count=1

    res=res+s[-1]+str(count)    # run for last charecter of string 

    return res


ans=String_RLE("abcabb")
print(ans)

