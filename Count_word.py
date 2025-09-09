# count word in a String 

def count_word(s):
    if s==" ":
        return None
    word_list=s.split(" ")
    count=0
    for word in word_list:  # without using for loop , we can use len() function to get num of word in a word_list
        count+=1
    return count


ans=count_word("The quick brown fox jumped over the lazy dog")
print(ans)