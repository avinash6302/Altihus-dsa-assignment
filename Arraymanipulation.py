
#kedanes alglorithm
def kedane(arr, n):
    s = -float('inf')
    e = 0
    for i in range(n):
        e = e+arr[i]
        if s < e:
            s = e
        if e < 0:
            e = 0
    return s

arr = list(map(int, input().split()))
print(kedane(arr, len(arr)))