import click
from click.testing import CliRunner


@click.command()
@click.option("--word", prompt=True)
def reverse(word):
    reversed_word = word[::-1]
    click.echo(f"Reversed word: {reversed_word}")


def test_prompts():
    result = CliRunner().invoke(reverse, input="Samuel\n")
    assert result.exception is None
    assert result.output == "Word: Samuel\nReversed word: leumaS\n"
