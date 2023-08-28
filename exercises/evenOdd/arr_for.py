def forSearchingEvenOdd(arr):
    pair = []
    odd = []
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0 :
            pair.append(arr[i])
        else :
            odd.append(arr[i])
    return pair, odd