import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("🟡 No tasks found.")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("✅ Task added!")
    else:
        print("⚠️ Task cannot be empty.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("🗑️ Task deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n🔹 TO-DO LIST MENU 🔹")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Progress saved. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
