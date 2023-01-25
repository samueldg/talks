import click


@click.command()
def print_output():
    click.echo('I am just normal text')
    click.echo(click.style('I am cyan!', fg='cyan'))
    click.secho('Christmas time!!!', bg='red', fg='green',
                underline=True, bold=True)


if __name__ == '__main__':
    print_output()
