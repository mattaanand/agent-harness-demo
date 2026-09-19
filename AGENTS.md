# Agent instructions

Small Python to-do library (`todo.py`) with tests (`test_todo.py`).

## Commands
- Verify all work: `make check` (runs ruff lint + pytest)
- Setup: `python3 -m venv .venv && source .venv/bin/activate && pip install pytest ruff`

## Rules
- Run `make check` before saying a task is done. Report its result honestly.
- Every new function needs at least one test in `test_todo.py`.
- Never edit or delete an existing test to make it pass. Fix the code instead.
- Do not add dependencies without asking.
- Do not modify `AGENTS.md`, `CLAUDE.md`, or `Makefile` unless the task says so.
- Keep changes small and focused on the task.
