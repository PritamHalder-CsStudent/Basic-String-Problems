# Frist non repeating character 
# example--> "swiss"---> Output: "w"

def Non_repeat(s):
    dd={}
    res=""
    for ch in s:
        dd[ch]=dd.get(ch,0)+1
    for ele in dd:
        if dd[ele] == 1 :
            return ele
    return None
        


ans= Non_repeat("swiss")
print(ans)
    
           


