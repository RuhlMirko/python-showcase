import os.path
import tkinter.filedialog

import ttkbootstrap as tb
import lorem

OUTPUTS_IMG = 'D:/Descargas/Horarios'

# root
root = tb.Window(themename='darkly')

# Center app on window
app_width = 500
app_height = 290
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) -(app_width/2))
y = int((screen_height/2) -(app_height/2))

root.geometry(f'{app_width}x{app_height}+{x}+{y}')


# styles
Style = tb.Style()
Style.configure('titleLabel.TLabel', font=('Segoe UI', 14, 'bold'))
Style.configure('em.TLabel', font=('Segoe UI', 10, 'italic'), foreground='#666')
Style.configure('TButton', font=('Segoe UI', 10))

# Title
title_lbl = tb.Label(text='Title of project', style='titleLabel.TLabel')
title_lbl.pack(pady=10)
summary_text = lorem.sentence()
summary_lbl = tb.Label(text=f'Thus {summary_text}', style='em.TLabel')
summary_lbl.pack()
summary_btn = tb.Button(root, text='Read more')
summary_btn.pack(pady=(0, 20))

# showcase
example_frame = tb.LabelFrame(root, text='Test')
example_frame.pack(pady=10)
title_lbl = tb.Label(example_frame, text='PDF Converter', style='titleLabel.TLabel')
title_lbl.pack(pady=30)



root.mainloop()