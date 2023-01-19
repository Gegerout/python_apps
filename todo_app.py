import tkinter as tk

def on_select(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    tasks.delete(index)
    print(f"{value} removed from list.")

def add_task():
    task = task_entry.get()
    tasks.insert(tk.END, task)
    task_entry.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do App")

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add", command=add_task)
add_button.pack()

tasks = tk.Listbox(root)
tasks.pack()

tasks.bind('<<ListboxSelect>>', on_select)

root.mainloop()

