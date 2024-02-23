"""todo app using tkinter"""
import tkinter as tk

def add_task():
    task = task_entry.get()
    priority = priority_var.get()   
    if task:
        task_list.insert(tk.END, f"[{priority}] {task}")   
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        pass

"""Create the main Tkinter window"""
root = tk.Tk()
root.title('To-Do List App')

""" Create a frame for task-related widgets"""
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

""" Create an entry widget for entering tasks"""
task_entry = tk.Entry(task_frame, width=40)
task_entry.grid(row=0, column=0, padx=5)

"""Create a dropdown for selecting task priority"""
priority_var = tk.StringVar()
priority_var.set("Low")
priority_dropdown = tk.OptionMenu(task_frame, priority_var, "Low", "average", "important")
priority_dropdown.grid(row=0, column=1, padx=5)

""" Create a button to add tasks """
add_button = tk.Button(task_frame, text='Add Task', width=10, command=add_task)
add_button.grid(row=0, column=2, padx=5)

"""Create a button to delete tasks"""
delete_button = tk.Button(task_frame, text='Delete Task', width=10, command=delete_task)
delete_button.grid(row=0, column=3, padx=5)

def mark_complete():
    """ Get the index of the selected task """
    index = task_list.curselection()[0]
    task = task_list.get(index)
    task_list.delete(index) 
    task_list.insert(index, f"[DONE] {task}")

mark_complete_button = tk.Button(task_frame, text='Mark Complete', width=15, command=mark_complete)
mark_complete_button.grid(row=0, column=4, padx=5)

""" Create a listbox to display tasks """
task_list = tk.Listbox(root, width=50)
task_list.pack(padx=10, pady=10)

"""Start the Tkinter event loop """
root.mainloop()
