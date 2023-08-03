from cards import Card


def pytest_generate_tests(metafunc):
    if "start_state_from_gen_test" in metafunc.fixturenames:
        metafunc.parametrize("start_state_from_gen_test", [
            "done",
            "in prog",
            "todo",
        ])


def test_finish(empty_db, start_state_from_gen_test):
    db = empty_db
    initial_card = Card(
        summary="write a book",
        state=start_state_from_gen_test,
    )
    index = db.add_card(initial_card)

    db.finish(index)

    card = db.get_card(index)

    assert card.state == "done"
