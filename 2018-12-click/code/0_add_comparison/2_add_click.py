import click


@click.command()
@click.argument("b", type=click.INT)
@click.argument("a", type=click.INT)
def add(a, b):
    click.echo(a + b)


if __name__ == "__main__":
    add()
