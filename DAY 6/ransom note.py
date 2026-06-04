#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
def canConstruct(ransomNote, magazine):
    char_count = {}
    
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in ransomNote:
        if char_count.get(char, 0) == 0:
            return False
        char_count[char] -= 1
    
    return True
