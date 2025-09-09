# count vowels and consonants of a given string 

def count_vowelsAndConsonants(s):
    vowels="AEIOUaeiou"
    Vcount=0
    Ccount=0
    for i in range(len(s)):
        if s[i] in vowels:
            Vcount+=1
        elif s[i]==" ":
            continue
        else:
            Ccount+=1


    print("num of vowels:",Vcount)
    print("num of consonants:",Ccount)


print(count_vowelsAndConsonants("practice make perfect"))    

                