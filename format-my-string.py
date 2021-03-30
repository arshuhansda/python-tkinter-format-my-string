import re
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Format your string')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter your string:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)

def copy_button(value):
    clip = tk.Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(value)
    clip.destroy()

def replace_values(given_string):
    given_string = re.sub("^[-+_+]$"," ",given_string)
    given_string = re.sub("[-_]+"," ",given_string)
    given_string = re.sub("[^a-zA-Z\s0-9]","",given_string)
    return given_string

def get_spiral_tap_case():
    label3 = tk.Label(root, text= " "*100)
    canvas1.create_window(200, 210, window=label3)
    x1 = entry1.get()
    result = replace_values(x1)
    result = "-".join(result.split()).lower().strip()
    label3 = tk.Label(root, text= result)
    canvas1.create_window(200, 210, window=label3)
    button_copy = tk.Button(text='Copy', command=copy_button(result), bg='navy', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 235, window=button_copy)


def get_snake_case():
    label4 = tk.Label(root, text= " "*100)
    canvas1.create_window(200, 260, window=label4)
    x1 = entry1.get()

    result = replace_values(x1)
    result = "_".join(result.split()).lower().strip()
    label4 = tk.Label(root, text= result)

    canvas1.create_window(200, 260, window=label4)
    button_copy = tk.Button(text='Copy', command=copy_button(result), bg='navy', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 285, window=button_copy)

button1 = tk.Button(text='Get Spiral Tap Case', command=get_spiral_tap_case, bg='royal blue', fg='white', font=('helvetica', 9, 'bold'))
button2 = tk.Button(text='Get Snake Case', command=get_snake_case, bg='royal blue', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(150, 180, window=button1)
canvas1.create_window(280, 180, window=button2)

root.mainloop()
