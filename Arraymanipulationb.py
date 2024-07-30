
def rotate(arr, s, e):
    while s <= e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1

def rotatearr(arr, n, k):
    rotate(arr, 0, k - 1)
    rotate(arr, k, n - 1)
    rotate(arr, 0, n - 1)
    

arr = list(map(int, input().split()))
k = int(input())
rotatearr(arr, len(arr), k)
print(arr)