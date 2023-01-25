import click


@click.command()
@click.option('--password', prompt=True, hide_input=True)
def password_length(password):
    click.echo(f'Your password has {len(password)} characters')


if __name__ == '__main__':
    password_length()
