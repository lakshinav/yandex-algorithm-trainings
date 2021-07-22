n,k = tuple(map(int, input().split()))
seq_n = list(map(int, input().split()))
seq_k = list(map(int, input().split()))

def left_bound(arr, key):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (right + left)//2
        if arr[mid] < key:
            left = mid
        else:
            right = mid
    return left

def right_bound(arr, key):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (right + left)//2
        if arr[mid] <= key:
            left = mid
        else:
            right = mid
    return right


def binsearch(arr, key):
    left = left_bound(arr, key)
    right = right_bound(arr, key)
    if right - left == 1:
        print('NO')
    elif right - left > 1:
        print('YES')
    else:
        print('Hmmm')

for item_k in seq_k:
    binsearch(seq_n, item_k)
