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
        os.system("shutdown -s -t 10 -c 因为TkOS用户要关机，所以将在10秒后关机。")

def cantclose():
    messagebox.showerror("系统","请在系统菜单关闭此程序。")

def go_to_uploader():
    webbrowser.open("https://space.bilibili.com/1473734923")

def cmd():
    def sent_command():
        get_command = input_command.get()
        if get_command == "version":
            messagebox.showinfo(message = "TkOS New 1.0\n开发版本\n不是最终效果，请等待正式版\n0.0.114514\n本程序已使用MIT证书。\nsystem:{}".format(platform.system()))
        elif get_command == "sysinfo":
            messagebox.showinfo(message="{}".format(platform.system()))
        elif get_command == 'goto windows cmd.exe':
            print("TkOS:Open app\"cmd.exe\"is succcessfully.\nIf you want to exit the cmd.exe,please insert the\"exit\"command to exit the cmd.exe")
            os.system('cmd')
        else:
            print("sorry, your command is not a vaild TkOS command.")
        input_command.delete(0,tkinter.END)

    command = tkinter.Toplevel()
    command.title("终端")
    tkinter.Label(command, text = '请输入终端命令：').grid(row = 0, column=0)
    input_command = tkinter.Entry(command)
    input_command.grid(row = 0, column = 1)
    ttk.Button(command, text = "OK", command = sent_command).grid(row = 0,column=2)

def lltang():
    def ok():
        get_answer = your_input.get()
        who_are_you = ['你叫什么名字？', '你是谁？']
        fucks = ['卧槽','他妈的', '屮', '艹','傻逼', '草泥马', '操你妈', '我日你仙人',\
           '我日你先人', 'Fuck', 'fuck','Shit','shit','bitch', 'Bitch']
        one = who_are_you in get_answer
        two = fucks in get_answer
        if one:
            messagebox.showinfo(message = "我是小小唐。")
        elif two:
            messagebox.showinfo(message = '说脏话是一种不对的行为。')
        else:
            messagebox.showinfo("NiShuoSha?",'你说啥？')

    '''我是小小唐，文字助手'''
    lltang = tkinter.Toplevel()
    lltang.title("小小唐")
    tkinter.Label(lltang, text = "哈喽啊，你想说些什么？").grid(row = 0, column = 0)
    your_input = tkinter.Entry(lltang)
    your_input.grid(row = 0, column = 1)
    ttk.Button(lltang, text = '提交', command = ok).gri(row = 0, column = 2)

def about():
    about_windows = tkinter.Toplevel()
    about_windows.title("关于TkOS")
    tkinter.Label(about_windows, text = 'TkOS New Version 1.0\n版本0.0.114514.1（开发版本2）\n制作者bilibili -小唐玩电脑-\n本程序使用MIT许可证。').pack()
    ttk.Button(about_windows, text = '官方网站', command = webbrowser.open("https://zqtang10/github.io/TkOS_New_1.0")).pack()
root = tkinter.Tk()
root.title('主界面')
root.protocol("WM_DELETE_WINDOW", cantclose)
menu = tkinter.Menu()
system = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = '系统(S)', menu = system)
system.add_command(label = '关机系统', command = shutdown)
system.add_command(label = "关机（注意这个真的会关机）", command = shutdown_windows)
system.add_separator()
system.add_command(label = '终端', command = cmd)
system.add_separator()
system.add_command(label = '关于',command = about)
root.config(menu = menu)
tkinter.Label(root, text = 'TkOS New 1.0 开发版\n制作者：bilibili up主-小唐玩电脑-\n三连再看，养成习惯').grid(row = 0,column=0)
ttk.Button(root, text = '去看看up主首页', command = go_to_uploader).grid(row = 1,column=0)
ttk.Button(root, text = '我是小小唐', command = lltang).grid(row = 1, column = 1)
root.mainloop()