# Reverse a string using python fun
a="Good morning!"
s=a[::-1]  #this string slicing method autometically reverse the string , : first colon select the entaire string and -1 read the string from rigth to left

print(s)



def reverse_String(s):    # String is immutable object so it can not be reverse inplace, so we need a empty string to perform reverse operation 
    rev=" "
    for ch in s:
        rev=ch+rev
    print(rev)     


s="pritam"
reverse_String(s)