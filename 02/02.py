import typer

def to_upper(name:str):
    print(name.upper())
    
if __name__ == '__main__':
    typer.run(to_upper)
