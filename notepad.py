import tkinter as tk
from tkinter import filedialog, messagebox


class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Notepad")
        self.master.geometry("600x400")

        self.text = tk.Text(self.master, undo=True)
        self.text.pack()

        self.current_file = ""
        self.create_menu()

    def create_menu(self):
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.destroy, accelerator="Alt+F4")

        self.edit_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")

    def open_file(self):
        self.text.delete("1.0", "end")
        filepath = filedialog.askopenfilename()
        self.current_file = filepath
        with open(filepath, 'r') as file:
            self.text.insert('1.0', file.read())

    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.text.get('1.0', 'end'))
        else:
            self.current_file = filedialog.asksaveasfilename(defaultextension=".txt")
            with open(self.current_file, 'w') as file:
                file.write(self.text.get('1.0', 'end'))

    def cut_text(self):
        self.text.event_generate("<<Cut>>")

    def copy_text(self):
        self.text.event_generate("<<Copy>>")

    def paste_text(self):
        self.text.event_generate("<<Paste>>")


root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
