import math

import click


math_utils = click.Group()


@math_utils.command()
def pi():
    click.echo(math.pi)


@math_utils.command()
@click.argument("addends", type=click.INT, nargs=-1)
def add(addends):
    click.echo(sum(addends))


@math_utils.command()
@click.argument("x", type=click.INT)
@click.option("--base", type=click.INT, default=math.e)
def log(x, base):
    click.echo(math.log(x, base))


if __name__ == "__main__":
    math_utils()
