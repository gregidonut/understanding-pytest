from cards import Card


def test_finish_from_in_prog(empty_db):
    db = empty_db
    index = db.add_card(
        Card(
            "second edition",
            state="in prog",
        )
    )
    db.finish(index)
    card = empty_db.get_card(index)
    assert card.state == "done"


def test_finish_from_done(empty_db):
    db = empty_db
    index = db.add_card(
        Card(
            "write a book",
            state="done",
        )
    )
    db.finish(index)
    card = empty_db.get_card(index)
    assert card.state == "done"


def test_finish_from_todo(empty_db):
    db = empty_db
    index = db.add_card(
        Card(
            "create a course",
            state="todo",
        )
    )
    db.finish(index)
    card = empty_db.get_card(index)
    assert card.state == "done"
