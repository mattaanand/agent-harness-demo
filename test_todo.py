from todo import add_task, complete_task, delete_task


def test_add_task():
    assert add_task([], "a") == [{"title": "a", "done": False}]


def test_complete_task():
    tasks = add_task([], "a")
    assert complete_task(tasks, "a")[0]["done"] is True


def test_delete_task():
    tasks = add_task(add_task([], "a"), "b")
    assert delete_task(tasks, "a") == [{"title": "b", "done": False}]


def test_delete_task_missing_title():
    tasks = add_task([], "a")
    assert delete_task(tasks, "zzz") == [{"title": "a", "done": False}]
