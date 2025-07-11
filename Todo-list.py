from tkinter import *
import tkinter as tk

window = tk.Tk()
window.geometry("800x200")
window.title("Your ToDo list")

class Task:
    def __init__(self,name,time):
        self.task_name = name
        self.task_time = time

class Todo:
    def __init__(self):
        self.tasks_list = []

    def add_task(self,task):
        popup = Toplevel(master=window)
        popup.geometry("300x200")
        popup.title("Add task")
        task_label = Label(master=popup, text="Enter the task here: ",font=("Arial", 12, "bold"))
        task_label.pack()

        task_entry = Entry(master=popup,font=('Arial',12))
        task_entry.pack()

        time_label = Label(master=popup, text="Enter time:",font=("Arial",12,"bold"))
        time_label.pack()

        time_entry = Entry(master=popup,font=("Arial",12))
        time_entry.pack()

        def submit_task():
            actual_task = task_entry.get()
            actual_time = time_entry.get()
            self.tasks_list.append(f"{actual_task} at {actual_time}")
            print("Task successfully added to the list")
            popup.destroy

        submit_button = Button(master=popup,text="Submit",font=("Arial",10),command=submit_task)
        submit_button.pack()
        
        return 
    
    def edit_task(self):
        edit_popup = Toplevel(master=window)
        edit_popup.geometry("300x100")
        edit_popup.title("Edit task")
        edit_label = Label(master=edit_popup, text="Edit task here: ")
        edit_label.pack()

        edit_entry = Entry(master=edit_popup, font=("Arial",12))
        edit_entry.pack()
        def submit_edit():
            edited_task = edit_entry.get()
            self.task = edited_task
            edit_popup.destroy
        submit_button = Button(master=edit_popup,text="Submit",font=("Arial",10),command=submit_edit)
        submit_button.pack()

    def show_task(self):
        show_popup = Toplevel(master=window)
        show_popup.geometry("400x200")
        show_popup.title("Your Tasks today")
        for task in self.tasks_list:
            var1 = IntVar()
            task_popup = Checkbutton(master=show_popup,text=f"{task}",variable=var1,font=("Arial",12,"bold"))
            task_popup.pack()

label = tk.Label(text="What are we going to do today?\n",font=("Arial", 18, "bold"))
label.pack()

task = Todo()

def create_task():
    task.add_task(task)

def edit_object():
    task.edit_task()

def showing_tasks():
    task.show_task()

add_button = tk.Button(window, text="Add tasks",font=("Arial", 12, "bold"),command=create_task)
edit_button = tk.Button(window,font=("Arial", 12, "bold"), text="Edit task", command=edit_object)
show_task_button = tk.Button(window, text="Show tasks",font=("Arial",12,"bold"),command=showing_tasks)
add_button.pack()
edit_button.pack()
show_task_button.pack()

window.mainloop()
