# Student Task Manager

A Python console application to manage student tasks, built to practise a complete Git and GitHub workflow.

## Features

- Add tasks (empty titles are rejected)
- Display all tasks with their completion status
- Mark tasks as completed
- Delete tasks by ID (invalid IDs are rejected)
- Automated unit tests run by GitHub Actions

## Setup

1. Install Python 3.10 or newer.
2. Clone the repository:

        git clone https://github.com/laibaamir-21/student-task-manager.git

3. Go into the project folder:

        cd student-task-manager

No extra packages are needed.

## Usage

Start the app:

    python main.py

Choose an option from the menu (1 to 5). See `docs/user-guide.md` for details.

## Running the tests

    python -m unittest discover -s tests -v

## License

MIT License. See the LICENSE file.

Project status: Completed
