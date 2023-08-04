import exercises_handler
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
        ctx.fail('Las cuatro variables(a,b,c y d) son requeridas')
    else:
        promedio = exercises_handler.exercise_1_2(a,b,c,d,e)
        print('Con las variables ', a, ',' ,b, ',',c, ',',d, ',',e, ',' , 'tenemos que el promedio es: ', promedio)

if __name__ == '__main__':
    cli()
