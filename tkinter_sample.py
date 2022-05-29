#!/usr/bin/env python
# -*- config: utf8 -*-
import sys
from tkinter import *

root = Tk()
root.title(u"本日の予定")
root.geometry("640x480")

Static1 = Label(text=u'本日の予定', foreground='#ff0000', background='#ffaacc', font=("Noto Sans CJK JP", "20", "bold"))
Static1.pack()

root.mainloop()



