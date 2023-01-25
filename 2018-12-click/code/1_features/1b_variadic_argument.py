import click


@click.command()
@click.argument('addends', type=click.INT, nargs=-1)
def add(addends):
    click.echo(sum(addends))


if __name__ == '__main__':
    add()
