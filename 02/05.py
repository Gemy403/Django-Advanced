import typer 
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def add():
    pass
@app.command()
def delete(username , confirm:Annotated[bool,typer.Option(prompt='Are You Sure ?')]):
    if confirm:
        print(f'deleting user : {username}')
        
    else:
        print('operation canceled')

if __name__ == "__main__":
    app()