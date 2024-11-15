# Task Tracker CLI

Task Tracker is a command-line interface (CLI) application to track and manage your tasks. With this tool, you can easily keep track of tasks you need to do, those you’re working on, and those that are already completed. This project is an excellent way to practice programming skills like handling user inputs, interacting with the filesystem, and managing JSON data.

Project url: https://roadmap.sh/projects/task-tracker

## Features

With Task Tracker, you can:

* **Add a new task**
* **Update or delete a task**
* **Mark tasks as "in-progress" or "done"**
* **List all tasks** or filter them by status (done, to-do, in-progress)

All tasks are stored in a JSON file within the current directory, making it easy to persist data without external libraries.

## Requirements

* **Command-line interface (CLI)** : The application runs directly from the command line.
* **User Actions and Inputs** : Accepts user actions and inputs as command-line arguments.
* **Data Storage** : Stores tasks in a JSON file, which will be created if it doesn’t exist.
* **Native Filesystem Support** : Uses the native file system module of the chosen programming language to interact with the JSON file.
* **Error Handling** : Gracefully handles errors and edge cases to ensure a smooth user experience.

## Installation

1. Clone the repository.

   ```
   git clone https://github.com/YourUsername/task-tracker-cli.git
   cd task-tracker-cli
   ```
2. Make the script executable (if applicable).

   ``chmod +x task-cli``
3. Run the `task-cli` command as described below.

## Usage

The application supports the following commands:

### Adding a New Task

To add a new task, use the `add` command:

```
task-cli add "Buy groceries"
# Output: Task added successfully
```

### Updating and Deleting Tasks

To update or delete a task by its ID, use `update` or `delete`:

```
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

```

Marking a Task as "In-Progress" or "Done"

To change a task’s status, use `mark-in-progress` or `mark-done`:

```
task-cli mark-in-progress 1
task-cli mark-done 1

```

Listing All Tasks

To list all tasks, use `list`:

```
task-cli list

```

Listing Tasks by Status

```
task-cli list done
task-cli list todo
task-cli list in-progress

```
