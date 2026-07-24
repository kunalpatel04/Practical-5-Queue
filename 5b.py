import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def set_size(self):
        try:
            self.size = int(size_entry.get())
            if self.size <= 0:
                raise ValueError
            messagebox.showinfo("Success", "Queue Size Set Successfully!")
            size_entry.config(state="disabled")
            set_btn.config(state="disabled")
        except:
            messagebox.showerror("Error", "Enter a valid queue size.")

    def enqueue(self):
        item = item_entry.get()

        if self.size == 0:
            messagebox.showerror("Error", "Set Queue Size First!")
            return

        if len(self.queue) == self.size:
            messagebox.showerror("Error", "Queue is Full!")
        elif item == "":
            messagebox.showwarning("Warning", "Enter an Item!")
        else:
            self.queue.append(item)
            item_entry.delete(0, tk.END)
            self.display()

    def dequeue(self):
        if len(self.queue) == 0:
            messagebox.showerror("Error", "Queue is Empty!")
        else:
            messagebox.showinfo("Dequeued", self.queue.pop(0))
            self.display()

    def peek(self):
        if len(self.queue) == 0:
            messagebox.showinfo("Peek", "Queue is Empty!")
        else:
            messagebox.showinfo("Front Item", self.queue[0])

    def traverse(self):
        if len(self.queue) == 0:
            messagebox.showinfo("Traverse", "Queue is Empty!")
        else:
            messagebox.showinfo("Queue", " -> ".join(self.queue))

    def check_empty(self):
        if len(self.queue) == 0:
            messagebox.showinfo("Status", "Queue is Empty")
        else:
            messagebox.showinfo("Status", "Queue is Not Empty")

    def check_full(self):
        if len(self.queue) == self.size:
            messagebox.showinfo("Status", "Queue is Full")
        else:
            messagebox.showinfo("Status", "Queue is Not Full")

    def display(self):
        listbox.delete(0, tk.END)
        for item in self.queue:
            listbox.insert(tk.END, item)


root = tk.Tk()
root.title("Queue Management System")
root.geometry("500x550")
root.resizable(False, False)

q = Queue()

tk.Label(root, text="QUEUE MANAGEMENT SYSTEM",
         font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Queue Size").pack()

size_entry = tk.Entry(root, width=20)
size_entry.pack()

set_btn = tk.Button(root, text="Set Size", command=q.set_size)
set_btn.pack(pady=5)

tk.Label(root, text="Enter Item").pack()

item_entry = tk.Entry(root, width=25)
item_entry.pack(pady=5)

tk.Button(root, text="Enqueue", width=18, command=q.enqueue).pack(pady=3)
tk.Button(root, text="Dequeue", width=18, command=q.dequeue).pack(pady=3)
tk.Button(root, text="Peek", width=18, command=q.peek).pack(pady=3)
tk.Button(root, text="Traverse", width=18, command=q.traverse).pack(pady=3)
tk.Button(root, text="Check Empty", width=18, command=q.check_empty).pack(pady=3)
tk.Button(root, text="Check Full", width=18, command=q.check_full).pack(pady=3)

listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

tk.Button(root, text="Exit", width=18, command=root.destroy).pack(pady=5)

root.mainloop()
