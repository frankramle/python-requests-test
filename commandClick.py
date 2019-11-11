import click
import subprocess

@click.command()
@click.argument('test')
def runTest(test):
    if test == 'test':
        print ('RUN TEST API')
        subprocess.call('pytest -s', shell=True)
    else:
        print('COMMAND INCORRECT | COMMAND CORRECT: beonit test')