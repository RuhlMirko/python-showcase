import ttkbootstrap as tb
import lorem
from showcase import *

OUTPUTS_IMG = 'D:/Descargas/Horarios'
current_proj = 0

# root
root = tb.Window(themename='darkly')

# Center app on window
app_width = 500
app_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_height / 2))

root.geometry(f'{app_width}x{app_height}+{x}+{y}')

# styles
Style = tb.Style()
Style.configure('titleLabel.TLabel', font=('Segoe UI', 14, 'bold'))
Style.configure('em.TLabel', font=('Segoe UI', 10, 'italic'), foreground='#666')
Style.configure('TButton', font=('Segoe UI', 10))

# Title
title_lbl = tb.Label(text=return_str()[0], style='titleLabel.TLabel')
title_lbl.pack(pady=10)
summary_text = lorem.sentence()
summary_lbl = tb.Label(text=return_str()[1], style='em.TLabel')
summary_lbl.pack()

# showcase
example_frame = tb.LabelFrame(root, text='Test Data')
example_frame.pack(pady=10)
proj_lbl = tb.Label(example_frame, text=return_str()[2])
proj_lbl.pack(padx=20, pady=10)

# Project cursor
nav_proj_frame = tb.Frame(root)
nav_proj_frame.pack(pady=10)


def moveProj(steps):
    global current_proj
    if current_proj > 0 or steps != -1:
        current_proj += steps
    print(current_proj)


prevProj = tb.Button(nav_proj_frame, text='Prev', width=10, bootstyle='outline-info', command=lambda: moveProj(-1))
nextProj = tb.Button(nav_proj_frame, text='Next', width=10, bootstyle='outline-info', command=lambda: moveProj(1))
prevProj.pack(side='left', padx=10)
nextProj.pack(side='right', padx=10)

root.mainloop()
