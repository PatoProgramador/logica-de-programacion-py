def sumMultiArrs(arr1, arr2):
    sum = []
    multi = []
    for i in range(0, len(arr1)):
        sum.append(arr1[i] + arr2[i])
        multi.append(arr1[i] * arr2[i])
    return sum, multi
