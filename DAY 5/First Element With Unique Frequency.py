#First Element With Unique Frequency    
#Given a list of integers, determine the first element whose frequency is unique.
#A frequency is considered unique if no other element in the list has the same frequency.
#If multiple elements have unique frequencies, print the one that appears first in the list.
#If no such element exists, print -1.
def first_unique_frequency(arr):
    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    freq_count = {}

    for freq in frequency.values():
        freq_count[freq] = freq_count.get(freq, 0) + 1

    for num in arr:
        if freq_count[frequency[num]] == 1:
            return num

    return -1


arr = [1, 2, 2, 3, 3, 3, 4]
print(first_unique_frequency(arr))
