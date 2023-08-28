from exercises.majorandminor.logical_operatos import integersMajorAndMinor, averageBetweenFloat
from exercises.majorandminor.for_cicle import forSearchingMajor
from exercises.evenOdd.arr_for import forSearchingEvenOdd
from exercises.sumMulti.sumMulti_Arrs import sumMultiArrs

def exercise_1(a,b,c,d):
    menor, mayor = integersMajorAndMinor(a,b,c,d)
    return menor,mayor

def exercise_1_2(a,b,c,d,e):
    promedio = averageBetweenFloat(a,b,c,d,e)
    return promedio

def exercise_2(arr):
    major = forSearchingMajor(arr)
    return major

def exercise_2_1(arr):
    pair, odd = forSearchingEvenOdd(arr)
    return pair, odd

def exercise_3(arr1, arr2):
    sum, multi = sumMultiArrs(arr1, arr2)
    return sum, multi
