import math

import click


@click.command()
def print_pi():
    click.echo(math.pi)


if __name__ == '__main__':
    print_pi()
