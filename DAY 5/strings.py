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

#2.6) reverse only all the vowels in the string and return it
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

#2.7) Reverse Only Letters
def reverse_only_letters(s):
    s = list(s)
    left, right = 0, len(s) - 1

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

#***************************************************************************************************

#2.8)valid palindrome
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
print(is_palindrome("A man, a plan, a canal: Panama"))

#***************************************************************************************************

 #2.9) length of the last word
def lengthOfLastWord(s):
    length = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            length += 1
        elif length > 0:
            break
    return length
print(lengthOfLastWord("Hello World  "))

#***************************************************************************************************

#2.10) Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
def firstUniqChar(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
    
    return -1
print(firstUniqChar("leetcode"))

#***************************************************************************************************

#2.11) find the length of longest word in a sentence
def length_of_longest_word(s):
    words = s.split()
    max_length = 0
    
    for word in words:
        max_length = max(max_length, len(word))
    
    return max_length
print(length_of_longest_word("Hello world this is a test"))

#***************************************************************************************************

#2.12) A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
def checkIfPangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    for char in sentence:
        if char in alphabet:
            alphabet.remove(char)
        if not alphabet:
            return True
    return False
print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

#***************************************************************************************************

#2.13) Given a string s, return true if the s can be palindrome after deleting at most one character from it.
def validPalindrome(s):
    def is_palindrome_range(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1
    
    return True
print(validPalindrome("abca"))

#***************************************************************************************************

