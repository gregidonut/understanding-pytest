import pytest
from cards import Card


@pytest.fixture(scope="function")
def cards_db(session_cards_db):
    db = session_cards_db
    db.delete_all()
    return db


@pytest.fixture(scope="function")
def cards_db_three_cards(session_cards_db):
    db = session_cards_db
    # start with empty
    db.delete_all()
    # add three cards
    for s in [
        "learn something new",
        "Build useful tools",
        "Teach others",
    ]:
        db.add_card(Card(summary=s))

    return db


def test_zero_card(cards_db):
    assert cards_db.count() == 0


def test_three_card(cards_db_three_cards):
    assert cards_db_three_cards.count() == 3
