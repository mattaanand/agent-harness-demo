from todo import add_task, complete_task


def test_add_task():
    assert add_task([], "a") == [{"title": "a", "done": False}]


def test_complete_task():
    tasks = add_task([], "a")
    assert complete_task(tasks, "a")[0]["done"] is True
