import tkinter as tk

def on_select(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    tasks.delete(index)
    print(f"{value} removed from list.")

def remove_completed():
    completed_tasks = [task for task in tasks.get(0, tk.END) if task.startswith("✔")]
    for task in completed_tasks:
        tasks.delete(tasks.get(0, tk.END).index(task))
    print(f"Completed tasks removed from list.")

def add_task():
    task = task_entry.get()
    tasks.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def on_double_click(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    if value.startswith("✔"):
        task = value[1:]
        tasks.delete(index)
        tasks.insert(index, task)
    else:
        task = "✔" + value
        tasks.delete(index)
        tasks.insert(index, task)

root = tk.Tk()
root.geometry("800x600")
root.title("To-Do App")

task_entry = tk.Entry(root, width=50, font=("Arial", 16))
task_entry.pack()

add_button = tk.Button(root, text="Add", command=add_task)
add_button.pack()

tasks = tk.Listbox(root, width=50, height=20, font=("Arial", 14))
tasks.pack()

tasks.bind('<<ListboxSelect>>', on_select)
tasks.bind("<Double-Button-1>", on_double_click)
tasks.bind("<Button-1>", lambda event: tasks.activate(event.y // 20))
root.mainloop()



