# longest word in a sentence 
# example --> "python is powerfull" ---> "powerfull"

def longest_word(s):
    word_list=s.split(" ")
    dd={}
    for word in word_list:
        dd[word]=dd.get(word,0)+len(word)
 
    ans=max(dd,key=dd.get) # we are finding max size word with max function respect of key as word dd.get=value of dict
    return ans


"""res=longest_word("The quick brown fox jumped over the lazy dog ")
print(res)
"""


# solving problem without use of dectionary  

def longest(s):
    word_list=s.split(" ")
    temp_word=" "
    for word in word_list:
        if len(word) > len(temp_word):
            temp_word=word
    return temp_word


ans=longest("python is powerfull")
print(ans)

