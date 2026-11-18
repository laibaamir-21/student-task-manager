# User Guide

## Starting the app

Open a terminal in the project folder and run `python main.py`.

## Menu options

1. **Add task:** type a title and press Enter. Empty titles are rejected with an error message.
2. **Show tasks:** lists every task. `[x]` means completed and `[ ]` means pending.
3. **Complete task:** enter the task ID shown in the list to mark it as completed.
4. **Delete task:** enter the task ID to remove that task.
5. **Exit:** closes the program.

## Notes

- Tasks are kept in memory, so they are cleared when you exit.
- If you enter a non-numeric ID, the app shows an error and returns to the menu.
- If you enter an ID that does not exist, the app reports that the task was not found.
