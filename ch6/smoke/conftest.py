import cards
import pytest


@pytest.fixture(scope="session")
def db(tmp_path_factory):
    """CardsDB object connected to a temporary database"""
    db_path = tmp_path_factory.mktemp("cards_db")
    db = cards.CardsDB(db_path)
    yield db
    db.close()


@pytest.fixture(scope="function")
def cards_db(db):
    """Empty db from tmp_path"""
    db.delete_all()
    return db
