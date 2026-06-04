#goat latin
# You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) 
# The rules of Goat Latin are as follows:
# If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
def goat_latin(s):
    vowels="aeiouAEIOU"
    l=s.split()
    count=1
    res=[]
    for i in range(len(l)):
        word=l[i]
        if word[0] in vowels:
            res.append(word+"ma"+"a"*count)
            count+=1
        else:
            res.append(word[1:]+word[0]+"ma"+"a"*count)
            count+=1
    return "".join(res)
print(goat_latin("spoorthi is upcoming hackthon winner"))
