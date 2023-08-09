import pytest

NUM_CARDS = 4


@pytest.mark.num_cards(NUM_CARDS)
def test_num_cards(cards_db):
    assert cards_db.count() == NUM_CARDS
