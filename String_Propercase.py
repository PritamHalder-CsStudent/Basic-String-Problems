# Proper case of string means = Every word start with capital letter 
# Example - "the lord of the rings" -->  "The Lord Of The Rings"

def String_Proper(s):
    substring_list=s.split(" ")  # convert the string into substring list , separate the element with respect of space present
    ans_list=[]
    for word in substring_list:
        ans_list.append(word.capitalize())     # capitalize() function convert 1st char of word into capital charecter
    return " ".join(ans_list)  # .join function taking a list object and convert into String object    
        
        
s=input("enter a string :")
ans=String_Proper(s)
print(ans)


