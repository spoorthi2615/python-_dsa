# .upper for upper case converstion
#.isuppper for checking vice versa for lower case also
#.index to find the index (find does not return error returns -1 but index does give error )
#String is inmutable use replace indexing replacing does not work 

#2.1) conversion to upper
def converstion_upper(s):
    upper_s=""
    for i in s:
        
        temp=ord(i)
        text=i
        if temp>=97:
            temp=temp-32
            text=chr(temp)
        upper_s=upper_s+text
    print(upper_s)

#***************************************************************************************************

#2.2) conversion to lower
def converstion_lower(s):
    lower_s=""
    for i in s:
        
        temp=ord(i)
        text=i
        if temp<=90:
            temp=temp+32
            text=chr(temp)
        lower_s=lower_s+text
    print(lower_s)

converstion_upper("Neha__")
converstion_lower("Neha__")
 
 #***************************************************************************************************

#2.3) vowel
def count_of_value(s):
    count=0
    vowel="aeiouAEIOU"
    for ch in s:
        if ch in vowel:
            count+=1
    print(count)
count_of_value("aeiousAEIOU")

#2.4) reverse string
def reverse_string(s):
    rev=""
    for i in s:
        rev=i+rev
    print(rev)
reverse_string("Neha")

#***************************************************************************************************

#2.5) reverse string special (only letters should be reversed, other characters should remain in the same position)
def reverse_string_special(s):
    s = list(s)

    left = 0
    right = len(s) - 1

    while left < right:

        if not s[left].isalpha():
            left += 1

        elif not s[right].isalpha():
            right -= 1

        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)

print(reverse_string_special("_Neha__"))

#***************************************************************************************************

#reverse only all the vowels in the string and return it
def reverse_vowels(s):
    s = list(s)
    vowels = "aeiouAEIOU"
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)
print(reverse_vowels("Neha__"))

#***************************************************************************************************