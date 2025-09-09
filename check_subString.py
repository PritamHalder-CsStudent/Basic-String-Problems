# check subString present in a String  
# Substring--> A substring is any sequence of characters that appears in the same order in the string .
# num of substring of a string is factorial of len(string),  ! len(string)
# Example--> String : "abc" --> substrings are a, ab, abc, b, bc, c 


# print all substring using for loop 
def print_Substring(s):
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            print(s[i:j])  


ans= print_Substring("abc")
print(ans)


# print all substring using recursion 

def print_subString_Recursion(s,start,end): 
    # base case : when start reach end of the string , we stop 
    if start == len(s):
        return
    # if end goes past the length of the string , it means all substring strating at start are printed
    # we move to next staring index  by incrementing start and reseating end  
    if end > len(s):   
        print_subString_Recursion(s,start=start+1,end=start+2)  
    else:                       # we print the current substring from start to end 
        print(s[start:end])
        print_subString_Recursion(s,start,end+1)    

s="xyz"
print_subString_Recursion(s,0,1)



# check substring present 
# Example :  Input: "openai" , Substring : "ai" --> True

def store_Substring(s):
    Substring_list=[]
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            Substring_list.append(s[i:j])
    return Substring_list        

        

def check_present_Substring(s,Ss):
    ans_list=store_Substring(s)
    for substr in ans_list:
        if substr == Ss:
            return True
    return False


ans=check_present_Substring("openai","ai")
print(ans)










