from cards import Card


def test_finish(empty_db):
    db = empty_db
    for c in [
        Card(
            "write a book",
            state="done",
        ),
        Card(
            "second edition",
            state="in prog",
        ),
        Card(
            "create a course",
            state="todo",
        ),
    ]:
        index = db.add_card(c)
        db.finish(index)
        card = db.get_card(index)
        assert card.state == "done"
