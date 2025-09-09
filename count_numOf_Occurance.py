# count occurances of a letters 

def count_Occurances(s):
    dd=dict()  # using dictionary we can easily count occurances of charecter
    for ele in s:
        dd[ele]=dd.get(ele,0) + 1   # if element not present in dictionary it will give 0 , otherwise it will give occurance 

    return dd

print(count_Occurances("programming"))    


# another way to write this function 
def char_frequency(s):
    feq={}  
    for ele in s:
        if ele in feq:
            feq[ele]=feq[ele]+1
        else:
            feq[ele]=1
    return feq

print(char_frequency("test"))            