#find the first negative number in every window of size k
from collections import deque

def firstNegative(arr, k):
    q = deque()
    result = []
    for i in range(len(arr)):
        if arr[i] < 0:
            q.append(i)
        while q and q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            if q:
                result.append(arr[q[0]])
            else:
                result.append(0)
    return result

# Example
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

print(firstNegative(arr, k))