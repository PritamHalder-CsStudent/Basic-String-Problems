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



# Updated version of the problem:

# Given a string S consisting of only lowercase and uppercase English letters and spaces, 
# your task is to convert it into title case. In title case, the first letter of each word is 
# capitalized while the rest are in lowercase, 
# except for words that are entirely in uppercase (considered as acronyms), which should remain unchanged.

# Sample test case :
# Input: this is a CODECHEF problem
# output: This Is A CODECHEF Problem


def convert_titleCase(s):
    str_arr = s.split(" ")

    for i in range(len(str_arr)):
        # If the entire word is uppercase (acronym), skip formatting
        if str_arr[i].isupper():
            continue
        # Otherwise convert to title-case (capital first letter, rest lowercase)
        str_arr[i] = str_arr[i].capitalize()

    return " ".join(str_arr)


t = int(input())
for _ in range(t):
    s = input()
    print(convert_titleCase(s))
