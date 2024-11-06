import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()  
    if task:  
        tasks.append(task)  
        entry.delete(0, tk.END)  
        update_listbox()  
    else:
        messagebox.showwarning("Warning", "You must enter a task.")  

def delete_task():
    try:
        task_index = listbox.curselection()[0]  
        del tasks[task_index]  
        update_listbox()  
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")  


frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=20,
    height=10,
    font=("Arial", 14),
    selectmode=tk.SINGLE,
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)


scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
