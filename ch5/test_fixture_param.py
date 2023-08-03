import pytest
from cards import Card


@pytest.fixture(params=[
    "done",
    "in prog",
    "todo",
])
def start_state(request):
    return request.param


def test_finish(empty_db, start_state):
    db = empty_db
    initial_card = Card(
        summary="write a book",
        state=start_state,
    )
    index = db.add_card(initial_card)

    db.finish(index)

    card = db.get_card(index)

    assert card.state == "done"
