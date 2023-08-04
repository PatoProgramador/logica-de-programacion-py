import exercises_handler
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--a', required=True, help='Primera variable')
@click.option('--b', required=True, help='Segunda variable')
@click.option('--c', required=True, help='Tercera variable')
@click.option('--d', required=True, help='Cuarta variable')
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

if __name__ == '__main__':
    cli()
