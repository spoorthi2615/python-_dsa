#compress the string
def compress_string(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))  # Append the last character and its count
    return ''.join(compressed)
s = "aaabbcaaa"
print(compress_string(s))

