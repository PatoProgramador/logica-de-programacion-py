import exercises.exercises_handler as exercises_handler
import click

@click.group()
def cli():
    pass
# Ejercicio 1, mayor y menor entre números enteros
@cli.command()
@click.option('--a', type=int, required=True, help='Primera variable')
@click.option('--b', type=int, required=True, help='Segunda variable')
@click.option('--c', type=int, required=True, help='Tercera variable')
@click.option('--d', type=int, required=True, help='Cuarta variable')
@click.pass_context
def exer1(ctx, a,b,c,d):
    if not a or not b or not c or not d:
        ctx.fail('Las cuatro variables(a,b,c y d) son requeridas')
    else:
        menor, mayor = exercises_handler.exercise_1(a,b,c,d)
        if a == b and a == c and a == d: 
            print('No existe número mayor o menor puesto que todas las variables son iguales')
        else:
            print('El número mayor es: ', mayor)
            print('El número menor es: ', menor)

# Ejercicio 1.2, promedio entre números flotantes
@cli.command()
@click.option('--a', type=float, required=True, help='Primera variable')
@click.option('--b', type=float, required=True, help='Segunda variable')
@click.option('--c', type=float, required=True, help='Tercera variable')
@click.option('--d', type=float, required=True, help='Cuarta variable')
@click.option('--e', type=float, required=True, help='Cuarta variable')
@click.pass_context
def exer1_2(ctx, a,b,c,d,e):
    if not a or not b or not c or not d or not e:
        ctx.fail('Las cinco variables(a,b,c,d y e) son requeridas')
    else:
        promedio = exercises_handler.exercise_1_2(a,b,c,d,e)
        print('Con las variables ', a, ',' ,b, ',',c, ',',d, ',',e, ',' , 'tenemos que el promedio es: ', promedio)

# Ejercico 2, busqueda del mayor y menor con un ciclo for
@cli.command()
@click.argument('array', nargs=-1, type=int, required=True, metavar='arr')
@click.pass_context
def exer2(ctx, array):
    if len(array) < 2:
        ctx.fail('No existe mayor o menor puesto que solo hay un valor')
    else:
        major = exercises_handler.exercise_2(array)
        print(f'El número mayor es: {major}')

# Ejercico 2.1, busqueda de numeros pares e impares
@cli.command()
@click.argument('array', nargs=-1, type=int, required=True, metavar='arr')
@click.pass_context
def exer2_1(ctx, array):
    if len(array) == 1:
        if array[0] % 2 == 0 :
            print(f'El unico número es par, siendo este: {array[0]}')
        else :
            print(f'El unico número es impar, siendo este: {array[0]}')
    elif len(array) == 0:
        ctx.fail('Debes pasar los números para hacer la búsqueda')
    else:
        pairs, odd = exercises_handler.exercise_2_1(array)
        print(f'Hay {len(pairs)} números pares los cuales son {pairs}')
        print(f'Hay {len(odd)} números impares los cuales son {odd}')

if __name__ == '__main__':
    cli()