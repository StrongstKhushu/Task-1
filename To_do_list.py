# CodSoft Internship Task 1
import tkinter as tk
import json
import os
file_name = "tasks.json"
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        tasks = json.load(f)
else:
    tasks = []
def save():
    with open(file_name, "w") as f:
        json.dump(tasks, f)

def show_tasks():
    listbox.delete(0, tk.END)
    for i, t in enumerate(tasks):
        status = "Complete" if t["done"] else "Incomplete"
        listbox.insert(tk.END, f"{i+1}. {t['title']} [{status}]")
def add_task():
    text = entry.get()
    if text != "":
        tasks.append({"title": text, "done": False})
        save()
        show_tasks()
        entry.delete(0, tk.END)
def task_done():
    index = listbox.curselection()
    if index:
        tasks[index[0]]["done"] = True
        save()
        show_tasks()
def delete_task():
    index = listbox.curselection()
    if index:
        tasks.pop(index[0])
        save()
        show_tasks()
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x350")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

btn1 = tk.Button(root, text="Add Task", command=add_task)
btn1.pack()

btn2 = tk.Button(root, text="Task Done", command=task_done)
btn2.pack()

btn3 = tk.Button(root, text="Delete Task", command=delete_task)
btn3.pack()

listbox = tk.Listbox(root, width=40, height=12)
listbox.pack(pady=10)

show_tasks()
root.mainloop()
