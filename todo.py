def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    return tasks


def complete_task(tasks, title):
    for t in tasks:
        if t["title"] == title:
            t["done"] = True
    return tasks
