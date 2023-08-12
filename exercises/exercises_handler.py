from exercises.majorandminor.logical_operatos import integersMajorAndMinor, averageBetweenFloat
from exercises.majorandminor.for_cicle import forSearchingMajor

def exercise_1(a,b,c,d):
    menor, mayor = integersMajorAndMinor(a,b,c,d)
    return menor,mayor

def exercise_1_2(a,b,c,d,e):
    promedio = averageBetweenFloat(a,b,c,d,e)
    return promedio

def exercise_2(arr):
    major = forSearchingMajor(arr)
    return major