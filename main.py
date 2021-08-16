import tkinter
from tkinter import messagebox
from tkinter import ttk
import os
import sys
import platform
import webbrowser

def shutdown():
    que = messagebox.askokcancel("提示",'你确定要关闭TkOS吗？')
    if que == True:
        sys.exit()

def shutdown_windows():
    que = messagebox.askokcancel("提示","你确信要关闭系统吗？\n注意这个真的会让Windows关机！")
    if que == True:
        os.system("shutdown -s -t 300 -c 因为TkOS用户要关机，所以将在10秒后关机。")

def cantclose():
    messagebox.showerror("系统","请在系统菜单关闭此程序。")

def go_to_uploader():
    webbrowser.open("https://space.bilibili.com/1473734923")

def about():
    messagebox.showinfo(message = "TkOS New 1.0\n开发版本\n不是最终效果，请等待正式版\n0.0.114514\n本程序已使用MIT证书。\nsystem:{}".format(platform.system()))

root = tkinter.Tk()
root.title('主界面')
root.protocol("WM_DELETE_WINDOW", cantclose)
menu = tkinter.Menu()
system = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = '系统(S)', menu = system)
system.add_command(label = '关机系统', command = shutdown)
system.add_command(label = "关机（注意这个真的会关机）", command = shutdown_windows)
system.add_separator()
system.add_command(label = '关于',command = about)
root.config(menu = menu)
tkinter.Label(root, text = 'TkOS New 1.0 开发版\n制作者：bilibili up主-小唐玩电脑-\n三连再看，养成习惯').grid(row = 0,column=0)
ttk.Button(root, text = '去看看up主首页', command = go_to_uploader).grid(row = 1,column=0)
root.mainloop()