# Frist non repeating character 
# example--> "swiss"---> Output: "w"

def Non_repeat(s):
    dd={}
    res=""
    for ch in s:
        dd[ch]=dd.get(ch,0)+1
    for key in dd:
        if dd[key] == 1 :
            return key
    return None
        
# In leetcode problem we return answer as index of the non repeating character , 
# so in place of return ele , use return s.index(key) that will give index of the non repeating character

ans= Non_repeat("swiss")
print(ans)
    
           


