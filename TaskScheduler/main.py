import time
import threading
from collections import deque


class Task:
    def __init__(self, task_id, task_function, delay):
        self.task_id = task_id
        self.task_function = task_function
        self.delay = delay
        self.execute_at = time.time() + delay

    def __lt__(self, other):
        return self.execute_at < other.execute_at


class TaskScheduler:
    def __init__(self):
        self.tasks = deque()  # Queue to store tasks
        self.lock = threading.Lock()  # Lock to synchronize access to the tasks queue
        self.event = threading.Event()  # Event to signal when a new task is added
        self.thread = threading.Thread(
            target=self._run)  # Thread to execute tasks
        self.thread.daemon = True
        self.thread.start()

    def add_task(self, task):
        with self.lock:
            self.tasks.append(task)  # Add task to the queue
            # Sort tasks based on execution time
            self.tasks = deque(sorted(self.tasks))
            self.event.set()  # Signal the event to wake up the task scheduler thread

    def _run(self):
        while True:
            self.event.wait()  # Wait for the event to be set
            with self.lock:
                if self.tasks:
                    now = time.time()
                    if self.tasks[0].execute_at <= now:
                        task = self.tasks.popleft()  # Get the next task to execute
                        task.task_function()  # Execute the task
                        self.event.clear()  # Clear the event to wait for the next task
                    else:
                        self.event.clear()  # Clear the event to wait for the next task
                        # Wait for the next task's execution time
                        self.event.wait(timeout=self.tasks[0].execute_at - now)
                else:
                    self.event.clear()  # Clear the event if there are no tasks


def example_task():
    print("Task executed at", time.ctime())


def main():
    scheduler = TaskScheduler()

    while True:
        print("\n1. Add Task")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task_id = input("Enter task ID: ")
            delay = int(input("Enter delay in seconds: "))
            task = Task(task_id, example_task, delay)
            scheduler.add_task(task)  # Add the task to the scheduler
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
