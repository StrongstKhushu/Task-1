# CodSoft Internship Task 2

import tkinter as tk
def click(event):
    global expression
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(expression))
            screen_var.set(result)
            expression = result
        except Exception as e:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    else:
        expression += text
        screen_var.set(expression)
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""
screen_var = tk.StringVar()

screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=8, relief="ridge", justify="right")
screen.pack(fill="x", ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side="top", pady=5)
    for btn_text in row:
        b = tk.Button(frame, text=btn_text, font="Arial 15", width=5, height=2)
        b.pack(side="left", padx=5)
        b.bind("<Button-1>", click)

root.mainloop()
