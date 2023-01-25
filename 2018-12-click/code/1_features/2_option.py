import math

import click


@click.command()
@click.argument('x', type=click.INT)
@click.option('--base', '-b', type=click.INT, default=math.e)
def log(x, base):
    click.echo(math.log(x, base))


if __name__ == '__main__':
    log()
