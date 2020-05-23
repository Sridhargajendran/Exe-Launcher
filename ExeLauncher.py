import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Exe Launcher 1.1")
apps = []

if os.path.isfile('save.txt'):
    with open("save.txt", 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        #print(tempApps)
        apps = [x for x in tempApps if x.strip()]

def addApps():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("Executables", "*.exe"), ("All Files", "*.*")))
    apps.append(filename)
    
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)

def deleteApps():
    top = tk.Toplevel()
    top.geometry('400x400')
    top.title("Delete App")
    global listbox
    listbox = tk.Listbox(top, selectmode = tk.SINGLE)
    for app in apps:
        listbox.insert(1, app)
    listbox.place(relwidth = 0.8, relheight = 0.7, relx = 0.1, rely = 0.1)
    btn = tk.Button(top, text = "Delete App", command = lambda:[deleteSelected(),top.destroy()])
    btn.place(relwidth = 0.4, relheight = 0.09, relx = 0.3, rely = 0.9)
    

# if os.path.isfile('save.txt'):
#     with open("save.txt", 'r') as f:
#         tempApps = f.read()
#         tempApps = tempApps.split(',')
#         def deleteSelected():
#             data = ''
#             for i in listbox.curselection():
#                 data = listbox.get(i)
#                 tempApps.remove(data)
#                 apps = [x for x in tempApps]
#                 for app in apps:
#                     label = tk.Label(frame, text = app)
#                     label.pack()       

def deleteSelected():
    data = ''
    for i in listbox.curselection():
        data = listbox.get(i)
        apps.remove(data)

        for widget in frame.winfo_children():
            widget.destroy()

        for app in apps:
            label = tk.Label(frame, text = app, bg = "gray")
            label.pack()

canvas = tk.Canvas(root, height = 600, width = 500, bg = "#000000")
canvas.pack()

frame = tk.Frame(canvas, bg = "white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

openfile = tk.Button(root, text = "Open App", padx = 10, pady = 5, fg = "#000000", bg = "white", command = addApps)
openfile.pack()

runapps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg = "#000000", bg = "white", command = runApps)
runapps.pack()

deleteApps = tk.Button(root, text = "Delete App", padx = 10, pady = 5, fg = "#000000", bg = "white", command = deleteApps)
deleteApps.pack()

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ',')