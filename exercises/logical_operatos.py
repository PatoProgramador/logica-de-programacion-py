
def integersMajorAndMinor(a,b,c,d):
    # Busqueda del menor
    if a <= b and a <= c and a <= d : 
        menor = a

    elif b < a and b <= c and b <= d :
        menor = b

    elif c < a and c < b and c <= d :
        menor = c

    elif d < a and d < b and d <= c :
        menor = d
    # Busqueda del mayor
    if a >= b and a >= c and a >= d : 
        mayor = a

    elif b > a and b >= c and b >= d :
        mayor = b

    elif c > a and c > b and c >= d :
        mayor = c

    elif d > a and d > b and d >= c :
        mayor = d
    return menor, mayor

def averageBetweenFloat(a,b,c,d,e) :
   suma = a + b + c + d + e
   promedio = suma / 5
   return promedio
