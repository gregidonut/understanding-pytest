from typer.testing import CliRunner
import cards


def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()


def test_run_cards():
    assert run_cards("version") == cards.__version__
