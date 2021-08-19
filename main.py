'''TkOS New 1.0源代码
作者：bilibili -小唐玩电脑-
相关视频只在B站发布。
本程序使用MIT许可证。'''


import tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
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
        elif get_command == 'run textedit':
            print("open textedit")
            text_edit()
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

def update_log():
    log = tkinter.Toplevel()
    log.title("版本更新日志")
    tkinter.Label(log, text = '当前版本：开发版本3\n内部版本0.0.114514.2').pack()
    update = tkinter.Text(log)
    update.pack()
    update_text = '版本更新日志（按版本编号从大到小排列）\n\
0.0.114514.3:\n\
完善部分UI。\n\
完善文本编辑。\n\
新增程序打开器。\n\
0.0.114514.2：\n\
更新了更新日志的查看。\n\
新增文本编辑。\n\
0.0.114514.1：\n\
新增终端。\n\
新增文字助手小小唐（目前有bug ）。\n\
更新关于页面。\n\
0.0.114514：\n\
无更新。'
    update.insert(tkinter.END, update_text)

def text_edit():
    def open():
        file_open = filedialog.askopenfile(title = '打开文件', parent = windows, filetypes = [("文本文档", '.txt', \
            '所有文档', '.*')])
        with open(file_open, 'r') as file:
            text.insert(tkinter.END, file)
            file.close()
    def save():
        file_text = text.get(1.0, tkinter.END)
        file_name = filedialog.asksaveasfile(title = '保存/另存为文件...', parent = windows, filetypes = \
            [("文本文档", '.txt'), ("所有文件", '.*')])
        if  not file_name:
            return
        with open(file_name, 'w') as file:
            file.write(file_text)
            file.close()

    def new():
        if text.get(1.0, tkinter.END) == '':
            text.delete(1.0, tkinter.END)
        else:
            want = messagebox.askquestion(message="是否要保存当前的文件？")
            if want == True:
                save()
    windows = tkinter.Toplevel()
    windows.title('TkOS文本编辑器')
    text = tkinter.Text(windows)
    text.pack()
    text_menu = tkinter.Menu(windows)
    file_menu = tkinter.Menu(text_menu, tearoff = 0)
    help_menu = tkinter.Menu(text_menu, tearoff = 0)
    text_menu.add_cascade(label = '文件(F)', menu = file_menu)
    file_menu.add_command(label = '新建', command = new)
    file_menu.add_command(label = '保存', command = save)
    file_menu.add_command(label = '另存为')
    file_menu.add_command(label = '打开')
    file_menu.add_separator()
    help_menu.add_command(label = '关于')
    windows.config(menu = text_menu)

def open_app():
    def ok():
        app_will_open = var.get()
        if app_will_open == "文本编辑":
            text_edit()
        elif app_will_open == "终端":
            cmd()

    app = tkinter.Toplevel()
    app.title("打开应用程序")
    tkinter.Label(app, text = '请选择应用程序：').pack()
    var = tkinter.StringVar()
    app_select = ttk.Combobox(app, textvariable=var)
    app_select['value'] = ('文本编辑', '终端')
    app_select.pack()
    ttk.Button(app ,text = '确定', command = ok).pack()

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
system.add_command(label = '打开应用程序', command = open_app)
system.add_separator()
system.add_command(label = '更新日志', command = update_log)
system.add_command(label = '关于',command = about)
root.config(menu = menu)
tkinter.Label(root, text = 'TkOS New 1.0 开发版\n制作者：bilibili up主-小唐玩电脑-\n三连再看，养成习惯').grid(row = 0,column=0)
ttk.Button(root, text = '去看看up主首页', command = go_to_uploader).grid(row = 1,column=0)
ttk.Button(root, text = '我是小小唐', command = lltang).grid(row = 1, column = 1)
root.mainloop()