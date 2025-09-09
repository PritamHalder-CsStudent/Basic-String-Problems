# String contains only digits 
# example : "12345" --->  True


def Only_digits(s):
    temp="0123456789"
    if s == "":                 # we can check s.isdigit() function 
        return False
    for ch in s:
        if ch not in temp:
            return False
    return True


ans=Only_digits("123456")
print(ans)