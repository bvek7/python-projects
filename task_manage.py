import sqlite3

# Database setup
con = sqlite3.connect("work.db")
cur = con.cursor()

# Fixed table creation
cur.execute("""
CREATE TABLE IF NOT EXISTS work (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    priority INTEGER,
    is_completed INTEGER
)
""")
con.commit()
con.close()


class Task:
    def __init__(self, description, priority, is_completed):
        self.description = description
        self.priority = priority
        self.is_completed = is_completed

    def add(self):
        # Fix the database connection and insertion query
        con = sqlite3.connect("work.db")
        cur = con.cursor()
        try:
            cur.execute("""
            INSERT INTO work (description, priority, is_completed)
            VALUES (?, ?, ?)
            """, (self.description, self.priority, self.is_completed))
            con.commit()
            print("Task added successfully!")
        except Exception as e:
            print(f"Error while adding task: {e}")
        finally:
            con.close()

    @staticmethod
    def view():
        # Fixed the view method
        con = sqlite3.connect("work.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM work")
            tasks = cur.fetchall()
            if tasks:
                print("\nTasks available:")
                for task in tasks:
                    status = "Completed" if task[3] == 1 else "Not Completed"
                    print(f"ID: {task[0]}, Description: {task[1]}, Priority: {task[2]}, Status: {status}")
            else:
                print("No tasks available.")
        except Exception as e:
            print(f"Error while fetching tasks: {e}")
        finally:
            con.close()

    def delete(self):
        # Fixed the delete method
        con = sqlite3.connect("work.db")
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM work WHERE id = ?", (self.id,))
            con.commit()
            print("Task deleted successfully!")
        except Exception as e:
            print(f"Error while deleting task: {e}")
        finally:
            con.close()


# Menu-driven program to add and view tasks
def task_manager_menu():
    while True:
        print("\nTask Manager Menu")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            description = input("Enter task description: ").strip()
            priority = int(input("Enter task priority (1-10): ").strip())
            is_completed = int(input("Is the task completed? (1 for Yes, 0 for No): ").strip())
            task = Task(description, priority, is_completed)
            task.add()
        elif choice == "2":
            Task.view()
        elif choice == "3":
            task_id = int(input("Enter the ID of the task to delete: ").strip())
            task = Task("", 0, 0)  # We only need an ID to delete, description and others aren't needed
            task.id = task_id
            task.delete()
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Task Manager
task_manager_menu()
