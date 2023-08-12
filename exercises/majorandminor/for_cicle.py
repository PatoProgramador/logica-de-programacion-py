def forSearchingMajor(arr):
    major = arr[0]
    for num in arr:
        if num > major:
            major = num
    return major