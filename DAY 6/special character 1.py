#Count the Number of Special Characters I
#You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
#Return the number of special letters in word
def countSpecialCharacters(word):
    char_count = {}
    
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1
    
    special_count = 0
    for char in char_count:
        if char.islower() and char.upper() in char_count:
            special_count += 1
    
    return special_count
    

