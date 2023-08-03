from typer.testing import CliRunner
import cards


def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()


def test_run_cards():
    assert run_cards("version") == cards.__version__


def test_patch_get_path(monkeypatch, tmp_path):

    monkeypatch.setattr(
        cards.cli,
        "get_path",
        lambda: tmp_path,
    )

    assert run_cards("config") == str(tmp_path)


def test_patch_home(monkeypatch, tmp_path):
    full_cards_dir = tmp_path / "cards_db"

    monkeypatch.setattr(
        cards.cli.pathlib.Path,
        "home",
        lambda: tmp_path,
    )

    assert run_cards("config") == str(full_cards_dir)
