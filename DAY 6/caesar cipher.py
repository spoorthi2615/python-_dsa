#ceaser cipher
def ceaser(s,k):
    new_string="" 
    for i in s:
        new_string+=chr(ord(i)-k)
    return new_string
print(ceaser("khoor",3))

    