import typer

app = typer.Typer()

@app.command()
def mysum(x:int,y:int):
    print(f"sum is {x+y}")


@app.command()
def multiply(x:int,y:int):
    print(f"multiply is {x*y}")

if __name__ == "__main__":
    app()