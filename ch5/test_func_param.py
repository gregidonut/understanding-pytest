import pytest
from cards import Card


@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ("write a book", "done"),
        ("second edition", "in prog"),
        ("create a course", "todo"),
    ],
)
def test_finish(empty_db, start_summary, start_state):
    db = empty_db
    initial_card = Card(
        summary=start_summary,
        state=start_state,
    )
    index = db.add_card(initial_card)

    db.finish(index)

    card = db.get_card(index)

    assert card.state == "done"
