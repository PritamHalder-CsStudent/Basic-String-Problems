# Title case of a Sreing = Gammertically Capitalize of the first letter of the word
# Example - "the lord of the rings" -->  "The Lord of the Rings"

def TitleCase(s):
    small_words=["of","the","a","an","on","at","for","and","or","by","to","in","form"]
    orginal_words=s.lower().split(" ")
    ans_list=[]
    first_word=True  # it is used to help find first word and used as flaged 
    for word in orginal_words:
        if first_word  or word not in small_words:
            ans_list.append(word.capitalize())
        else:
            ans_list.append(word)
        first_word=False
    return " ".join(ans_list)


s="the lord of the rings"
ans=TitleCase(s)
print(ans)
