# Remove duplicate from the given string 
# Example= Programming --> programing

def remove_duplicate(s):
    res=" "
    seen=set()
    for ele in s:
        if ele not in seen:
            seen.add(ele)
            res+=ele
    return res


ans=remove_duplicate("programming")
print(ans)
