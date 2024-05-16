# same as decorator

import typer

def mysum(x:int,y:int):
    print(x+y)
    
def mul(x:int,y:int):
    print(x*y)

if __name__ == '__main__':
    app = typer.Typer()
    app.command()(mysum)
    app.command()(mul)
    app()