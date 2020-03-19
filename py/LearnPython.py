#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

__author__ = 'J'

# 创建多功能按键，修改tk图标
'''
import tkinter as tk


class Window:
    def __init__(self, title='nms', width=300, height=120, staFunc=bool, stoFunc=bool):
        self.w = width
        self.h = height
        self.stat = True
        self.staFunc = staFunc
        self.stoFunc = stoFunc
        self.staIco = None
        self.stoIco = None

        self.root = tk.Tk(className=title)

    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int( (ws/2) - (self.w/2) )
        y = int( (hs/2) - (self.h/2) )
        self.root.geometry(''{}'x'{}'+'{}'+'{}''.format(self.w, self.h, x, y))

    def packBtn(self):
        self.btnSer = tk.Button(self.root, command=self.event, width=15, height=3)
        self.btnSer.pack(padx=20, side='left')
        btnQuit = tk.Button(self.root, text='关闭窗口', command=self.root.quit, width=15, height=3)
        btnQuit.pack(padx=20, side='right')

    def event(self):
        self.btnSer['state'] = 'disabled'
        if self.stat:
            if self.stoFunc():
                self.btnSer['text'] = '启动服务'
                self.stat = False
                self.root.iconbitmap(self.stoIco)
        else:
            if self.staFunc():
                self.btnSer['text'] = '停止服务'
                self.stat = True
                self.root.iconbitmap(self.staIco)
        self.btnSer['state'] = 'active'

    def loop(self):
        self.root.resizable(False, False)   #禁止修改窗口大小
        self.packBtn()
        self.center()                       #窗口居中
        self.event()
        self.root.mainloop()

########################################################################
def sta():
    print('start.')
    return True
def sto():
    print('stop.')
    return True

if __name__ == '__main__':
    import sys, os

    w = Window(staFunc=sta, stoFunc=sto)
    w.staIco = os.path.join(sys.exec_prefix, 'DLLs\pyc.ico')
    w.stoIco = os.path.join(sys.exec_prefix, 'DLLs\py.ico')
    w.loop()
'''
# 登录界面
'''
import tkinter as tk


class Application:
    def __init__(self, root):
        self.root = root
        self.createFrameTop()
        self.createFrameButton()

    def createFrameTop(self):
        self.top_label = tk.Label(self.root, text="平台管理系统", fg="blue", bg="yellow", font=("Tempus Scas ITC", 20))
        self.top_label.grid(row=0, column=0, padx=15, pady=2)

    def createFrameButton(self):
        self.frame_button = tk.LabelFrame(self.root)
        self.frame_button.grid(row=1, column=0, padx=15, pady=2)

        # 创建文本“用户名”以及用户名输入框
        self.username_label = tk.Label(self.frame_button, text="用户名", font=("Tempus Sans ITC",15))
        self.username_label.grid(row=1, column=0, padx=15, pady=2, sticky='e')
        self.strvar = tk.StringVar()
        self.username_entry = tk.Entry(self.frame_button, textvariable=self.strvar)
        self.strvar.set("username")
        self.username_entry.grid(row=1, column=1, padx=15, pady=2)

        # 创建文本“密码”以及密码输入框
        self.key_label = tk.Label(self.frame_button, text="密  码", font=("Tempus Sans ITC", 15))
        self.key_label.grid(row=2, column=0, padx=15, pady=2, sticky='e')
        self.key_entry = tk.Entry(self.frame_button, show='*')
        self.key_entry.grid(row=2, column=1, padx=15, pady=2)

        # 显示“显示密码”勾选框
        self.flag_of_toggle = tk.IntVar()
        self.toggle_cbtn = tk.Checkbutton(self.frame_button, text="显示密码", variable=self.flag_of_toggle).grid(row=3, column=1, padx=1, sticky='e')

        self.login_btn = tk.Button(self.frame_button, relief=tk.GROOVE, text="Login", bd=2, command=lambda: print("Login successfully !"))
        self.login_btn.grid(row=4, column=1, padx=15, pady=2, sticky='e')


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Login")
    login = Application(root)
    root.mainloop()
'''
# 滚动条
'''
import tkinter as tk


class Application:
    def __init__(self, root):
        self.root = root
        self.createFrameTop()
        self.createFrameBottom()

    def createFrameTop(self):
        self.frm_top = tk.LabelFrame(self.root)
        self.frm_top.grid(row=0, column=0)

        self.frm_top_text_0 = tk.Text(self.frm_top, width=48, heigh=8, bg='purple', fg='blue')
        self.frm_top_text_0.grid(row=0, column=0)
        self.frm_top_scroll_0 = tk.Scrollbar(self.frm_top, orient=tk.VERTICAL, command=self.frm_top_text_0.yview)
        self.frm_top_text_0["yscrollcommand"] = self.frm_top_scroll_0.set
        self.frm_top_scroll_0.grid(row=0, column=0, sticky='wsen')

        for item in (range(1, 31)):
            self.frm_top_text_0.insert("end", str(item)+'\n')
            self.frm_top_text_0.see("end")

    def createFrameBottom(self):
        self.frm_bottom_0 = tk.LabelFrame(self.root)
        self.frm_bottom_0.grid(row=1, column=0)

        self.frm_bottom_listbox_0 = tk.Listbox(self.frm_bottom_0, width=25, height=4, font=('Tempus Sans ITC', 15))
        self.frm_bottom_listbox_0.grid(row=0, column=0, padx=5, pady=2, sticky='e')
        self.frm_bottom_scroll_0 = tk.Scrollbar(self.frm_bottom_0, orient=tk.VERTICAL, command=self.frm_bottom_listbox_0.yview)
        self.frm_bottom_listbox_0["yscrollcommand"] = self.frm_bottom_scroll_0.set
        self.frm_bottom_scroll_0.grid(row=0, column=1, sticky='swen')

        self.frm_bottom_listbox_0.insert("end", "Try double click here ^_^")
        self.frm_bottom_listbox_0.insert("end", 1)
        self.frm_bottom_listbox_0.insert("end", 2)
        self.frm_bottom_listbox_0.bind('<Double-Button-1>', lambda event: print(self.frm_bottom_listbox_0.get(self.frm_bottom_listbox_0.curselection())))

    def print_list(self, event):
            cur_string = self.frm_bottom_listbox_0.get(self.frm_bottom_listbox_0.curselection())
            print(cur_string)


        # for item in list(range(30)):
        #     self.frm_bottom_listbox_0.insert("end", item)
        # self.frm_bottom_listbox_0.bind('<Double-Button-1>', self.print_list)

    # def print_list(self, event):
    #     cur_string = self.frm_bottom_listbox_0.get(self.frm_bottom_listbox_0.curselection())
    #     self.frm_top_text_0.insert("end", cur_string)
    #     self.frm_top_text_0.see("end")


if __name__ == "__main__":
    root = tk.Tk()
    root.title('测试窗口')
    Application(root)
    root.mainloop()
'''
# Canvas半成品
'''
# canvas画布
import tkinter as tk

class CanvasDemo:
    def __init__(self):
        window = tk.Tk()
        window.title(" Canvas Demo ")
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        btRectangle = tk.Button(frame, text="rectangle", command=self.displayRect)
        btOval = tk.Butotn(frame, text="Oval", command=self.displayOval)
        vtPolygon = tk.Button(frame, text="Polygon", command=self.)
'''
# Canvas画图
'''
import tkinter as tk

root = tk.Tk()
root.title("Canvas Demo")
canvas = tk.Canvas(root, width=400, height=600, bg="white")
canvas.grid()
frame = tk.Frame(root)
frame.grid(row=1)

def displayDraw():
    canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")

def shadeDraw():
    canvas.delete("oval")

btn_of_Show = tk.Button(frame, text="Have a try", command=displayDraw)
btn_of_Show.grid(row=0, column=0, padx=50, sticky='w')
btn_of_Shade = tk.Button(frame, text="Shade", command=shadeDraw)
btn_of_Shade.grid(row=0, column=0, padx=20, sticky='e')

root.mainloop()
'''
# Toplevel, messagebox, filedialog的使用
'''
import tkinter as tk
from tkinter.messagebox import askquestion
from tkinter.messagebox import showerror
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfile
from tkinter import filedialog



class Application:
    def __init__(self, root):
        self.root = root
        self.createFrameTop()

    def createFrameTop(self):
        btn_toplevel = tk.Button(self.root, text="TopLevel", command=self.btn_toplevel_click)
        btn_toplevel.grid(row=0, column=0, padx=30, pady=30, sticky="wsen")

    def btn_toplevel_click(self):
        func_list = ["askquestion", "showerror", "asksaveasfilename", "askopenfile"]
        self.frm_toplevel = tk.Toplevel(self.root)
        self.frm_toplevel.title("TopLevel")
        for (count, func_name) in enumerate(func_list):
            btn = tk.Button(self.frm_toplevel, width=25, text=func_name)
            btn.grid(row=count//2, column=2*(count%2), padx=5, pady=5)
            btn.bind("<ButtonRelease-1>", self.Popup_window)

    def Popup_window(self, event):
        btn_txt = event.widget["text"]
        if btn_txt == "askquestion":
            if askquestion("choose", "choose yes or no", parent=self.frm_toplevel) == 'yes':
                print("your choose yes")
            else:
                print("you choose no")
        elif btn_txt == "showerror":
            showerror("error!", "show error!", parent=self.frm_toplevel)
        elif btn_txt == "asksaveasfilename":
            saveasfilename = asksaveasfilename()
            print(saveasfilename)
        elif btn_txt == "askopenfile":
            openfilename = askopenfile(filetypes=(("txt files", "*.txt"), ("All files", "*.*")))
            print(str(openfilename))
        self.frm_toplevel.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("XXX")
    Application(root)
    root.mainloop()
'''
# 弹窗测试
'''
import tkinter as tk
import tkinter.messagebox as msg
import tkinter.filedialog as fdlg

root = tk.Tk()
outer_frame = tk.LabelFrame(root)
outer_frame.grid()
# place a button for popup a message windows
def popupInfo():
    msg.showinfo(title="信息", message="成功弹出一个消息框！")
    msg.showerror(title="错误", message="成功弹出一个错误框")
    msg.showwarning(title="警报", message="成功弹出一个警报框")
btn_for_msginfo = tk.Button(outer_frame, text="Popup a msginfo", command=popupInfo).grid(padx=15, sticky="wsen")
def popupAsk():
    # if msg.askokcancel(title="取消", message="是否取消？")
    if msg.askquestion(title="问题", message="3+4是不是等于7") == 'no':
        msg.showerror(title="错误", message="恭喜你答错了")
    else:
        msg.showinfo(title="正确", message="恭喜你答对了")
btn_for_msgask = tk.Button(outer_frame, text="Popup a msgask", command=popupAsk).grid(row=1, padx=15, sticky="wsen")
btn_for_exit = tk.Button(outer_frame, text="Exit", command=root.destroy).grid(row=2, padx=15, sticky="wsen")
root.mainloop()
'''
# notebook和Radiobutton的使用(包括了Canvas)
'''
import tkinter as tk
import tkinter.ttk as ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        # self.root = root
        tk.Frame.__init__(self, master)
        self.grid()
        self.createNotebook()

    def createNotebook(self):
        self.frmNotebook = tk.LabelFrame(self, text="Notebook")
        self.frmNotebook.grid(sticky="swen")
        notebook = ttk.Notebook(self.frmNotebook)

        self.frmOne = tk.Frame(notebook)
        self.frmTwo = tk.Frame(notebook)
        self.frmThree = tk.Frame(notebook)
        self.frmFour = tk.Frame(notebook)
        self.frmFive = tk.Frame(notebook)

        notebook.add(self.frmOne, text='one', padding=3)
        notebook.add(self.frmTwo, text='Two', padding=3)
        notebook.add(self.frmThree, text='Three', padding=3)
        notebook.add(self.frmFour, text='Four', padding=3)
        notebook.add(self.frmFive, text='Five', padding=3)

        Row = 11
        Col = 11
        Width = 650
        table_name = 'tab one'

        element_header = []
        for i in range(Col):
            element_header.append(str(i))

        element_list = []
        for i in range(Row):
            element_list.append([])
            for j in range(Col):
                element_list[i].append(j)

        self.my_func(self.frmOne, Row, Col, element_header, element_list, Width, table_name)
        notebook.grid(row=0, column=0, sticky="wsen")

    def my_func(self, master, Row, Col, element_header, element_list, Width, table_name):
        self.frmTempTest = tk.LabelFrame(master, text=table_name)
        self.frmTempTest.grid(row=0, column=0, sticky='wsen')

        self.frmTempTestPart = tk.Canvas(self.frmTempTest, scrollregion=(0, 0, 50*Col, 17*Row), width=Width, height=300)
        self.frmTempTestPart.grid(row=0, column=0, sticky='swen')

        self.frmMyTableText = tk.Text(self.frmTempTestPart, width=6*Col, height=Row, insertbackground='red')
        self.frmTempTestPart.create_window(0, 0, window=self.frmMyTableText, height=17*Row, width=60*Col, anchor='nw')

        self.frmMyTableText.tag_config('a', background='springgreen', foreground='white')
        self.frmMyTableText.tag_config('b', background='lightgray')
        self.frmMyTableText.tag_config('c', background='white')
        for i in range(len(element_list)):
            for j in range(len(element_list[0])):
                my_str = "%6s"%element_list[i][j]

                if i == 0:
                    self.frmMyTableText.insert("end", str("%6s"%j), 'a')
                elif j == 0:
                    self.frmMyTableText.insert("end", str("%6s"%i), 'a')
                else:
                    if i%2 == 0:
                        self.frmMyTableText.insert("end", my_str, 'b')
                    else:
                        self.frmMyTableText.insert("end", my_str, 'c')
                if j == len(element_list[0])-1:
                    self.frmMyTableText.insert("end", '\n')

        #bind scrollbar
        self.scrolly = ttk.Scrollbar(master, orient=tk.VERTICAL, command=self.frmTempTestPart.yview)
        self.scrollx = ttk.Scrollbar(master, orient=tk.HORIZONTAL, command=self.frmTempTestPart.xview)
        self.frmTempTestPart["xscrollcommand"] = self.scrollx.set
        self.frmTempTestPart["yscrollcommand"] = self.scrolly.set
        self.scrolly.grid(row=0, column=1, sticky='swen')
        self.scrollx.grid(row=1, column=0, sticky='swen')

        #---------------------------
        self.frmOpenTestPart2 = tk.LabelFrame(self.frmOne, text='RadioBtn')
        self.frmOpenTestPart2.grid(row=0, column=2, sticky="swen")
        #---------------------------
        self.OpenTestrdovar = tk.IntVar()
        self.My_ButtonOpenTestCheckStandard = tk.Radiobutton(self.frmOpenTestPart2, variable=self.OpenTestrdovar, text='rbtn_0', value=21, command=None)
        self.My_ButtonOpenTestCheckStandard.grid(row=0, column=0, padx=3, pady=3, sticky='w')
        self.My_ButtonOpenTestCheckRowDiff = tk.Radiobutton(self.frmOpenTestPart2, variable=self.OpenTestrdovar, text='rbtn_1', value=22, state='disabled', command=None)
        self.My_ButtonOpenTestCheckRowDiff.grid(row=1, column=0, padx=3, pady=3, sticky='w')
        self.My_ButtonOpenTestCheckColDiff = tk.Radiobutton(self.frmOpenTestPart2, variable=self.OpenTestrdovar, text='rbtn_2', value=23, state='normal', command=lambda: print('You has checked radiobutton3'))
        self.My_ButtonOpenTestCheckColDiff.grid(row=2, column=0, padx=3, pady=3, sticky='w')
        self.OpenTestrdovar.set(21)

if __name__ == '__main__':
    # root = tk.Tk()
    # root.title("Notebook")
    app = Application()
    app.master.title('heiheihei')
    app.mainloop()
'''
# 显示按键名字
'''
import tkinter as tk


class Application:
    def __init__(self, root):
        self.root = root
        self.root.bind("<KeyPress>", self.bind_key)
        self.root.bind("<Shift_R>", self.bind_x_key)
        self.root.bind("<Control-q>", lambda event: root.destroy())

    def bind_key(self, event):
        print(event.keysym)

    def bind_x_key(self, event):
        print("!!!!!!!")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("key")
    Application(root)
    root.mainloop()
'''
# Text多功能测试
'''
import tkinter as tk

root = tk.Tk()
frm_general = tk.LabelFrame(root, text='Text')
frm_general.grid()
text = tk.Text(frm_general, width=30, height=4)
text.grid()
text.insert("insert", 'I love')

def show():
    print("哟吼，老子被点了一下")

btn = tk.Button(text, text='点老子试试', command=show)
text.window_create("insert", window=btn)

photo = tk.PhotoImage(file=r"K:\驱动备份（驱动精灵）\backup\Synaptics Pointing Device\synpd.inf_amd64_neutral_b76cc7ee7d253686\TP4-NOTE.GIF")
def showMotor():
    text.image_create("end", image=photo)

btn_pic = tk.Button(text, text='小图片', command=showMotor)
text.window_create("insert", window=btn_pic)

text.config(height=10)

root.mainloop()
'''
# 打开新窗口后隐藏原窗口
'''
import tkinter as tk

class Application:
    def __init__(self, root):
        self.root = root
        self.createMainFrame()

    def createMainFrame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        btn = tk.Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()

    def hide(self):
        self.root.withdraw()

    def openFrame(self):
        self.hide()
        otherFrame = tk.Toplevel()
        otherFrame.geometry("400x300")
        otherFrame.title("otherframe")
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        btn = tk.Button(otherFrame, text='close', command=handler)
        btn.pack()
        otherFrame.bind_all("<Destroy>", self.show)

    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()

    def show(self, event=None):
        self.root.update()
        self.root.deiconify()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Main frame")
    root.geometry("800x600")
    Application(root)
    root.mainloop()
'''
# Entry输入内容的获取
'''
import tkinter as tk

root = tk.Tk()
frmtop = tk.LabelFrame(root)
frmtop.grid()
e = tk.StringVar()
entry_account = tk.Entry(frmtop,  show='*', textvariable=e)
e.set("ti123")
entry_account.grid()
v = tk.IntVar()
ckbtn = tk.Checkbutton(frmtop, text='显示密码', variable=v)
ckbtn.grid(row=1, column=0, sticky='w', padx=10)
btn_login = tk.Button(frmtop, text='Login', command=lambda: print(entry_account.get(), e.get()))
btn_login.grid(row=1, sticky='e', padx=5)

def show_password(event):
    if v.get():

        entry_account.config(show='*')
        print(v.get())
    else:
        entry_account.config(show='')
        print(v.get())
ckbtn.bind("<Button-1>", show_password)

root.mainloop()
'''
# Label中插入图片，class操作出问题，图片无法显示！
'''
#  import tkinter as tk
# filename = 'F:/python/无标题.gif'
# root = tk.Tk()
# img = tk.PhotoImage(file=filename)
# label = tk.Label(root, image=img)
# label.pack()
# root.mainloop()
import tkinter as tk

# 很奇怪显示不出图片来
class Application():
    def __init__(self, root):
        self.root = root
        self.createWidget()

    def createWidget(self):
        frm_top = tk.LabelFrame(self.root, text='image')
        frm_top.pack()
        img = tk.PhotoImage(file='F:/python/无标题.gif')
        label = tk.Label(frm_top, image=img)
        label.pack()

root = tk.Tk()
window = Application(root)
root.mainloop()
'''
# Scale组件的使用
'''
import tkinter as tk

root = tk.Tk()
s1 = tk.Scale(root, from_=0, to=100, tickinterval=100, resolution=1, length=100)
s1.grid(row=0, column=0, sticky='w')
# s1.pack()
s2 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
s2.grid(row=1, column=0, sticky='s')
# s2.pack()
btn = tk.Button(root, text='Get position', command=lambda: print(s1.get(), s2.get()))
btn.grid(row=1, column=1, sticky='e', padx=10)
# btn.pack()
labeltext = tk.Label(root, text="当前位置：")
labeltext.grid(row=2, column=0, sticky='w')
labelPos = tk.Label(root, text="0,0", width=6)
labelPos.grid(row=2, column=0, sticky='w', padx=80)


def getPos(event):
    labelPos.config(text=str(s1.get())+','+str(s2.get()))

s1.bind("<B1-Motion>", getPos)
s2.bind("<B1-Motion>", getPos)
root.mainloop()
'''
# 验证的使用，不推荐使用！
'''
import tkinter as tk

root = tk.Tk()
def test():
    if e1.get() == '大傻逼':
        print('正确')
        return True
    else:
        print("错误")
        e1.delete(0, tk.END)
        return False

v= tk.StringVar()
e1 = tk.Entry(root, textvariable=v, validate='focusout', validatecommand=test)
e1.pack(padx=10, pady=10)
root.mainloop()
'''
# 两种下拉列表，tk.OptionMenu和ttk.Combobox
'''
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
v1 = tk.StringVar()
v1.set('one')
optmenu1 = tk.OptionMenu(root, v1, 'one', 'two', 'three')
optmenu1.pack()
btn1 = tk.Button(root, text='Get Option from menu1', command=lambda: print(v1.get()))
btn1.pack()

v2 = tk.StringVar()
v2.set('1')
optmenu2 = ttk.Combobox(root, textvariable=v2, value=list(range(1, 101)), width=5)
optmenu2.pack()
btn2 = tk.Button(root, text='Get Option from menu2', command=lambda: print(v2.get()))
btn2.pack()
tk.mainloop()
'''
# 菜单的使用
'''
import tkinter as tk
from tkinter import ttk

def donothing():
    filewin = tk.Toplevel(root)
    button = tk.Button(filewin, text='Do nothing button', command=filewin.destroy)
    button.pack()

root = tk.Tk(className='wodetest')
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)

cmdlist_for_file = ['New', 'Open', 'Save', 'Save as', 'Close']
for cmd in cmdlist_for_file:
    filemenu.add_command(label=cmd, command=donothing)

filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.destroy)
filemenu.add_radiobutton(label='sb1', value=0, command=lambda: print('sb 1'))
filemenu.add_radiobutton(label='sb2', value=1, command=lambda: print('sb 2'))
v = tk.IntVar()
def ckbtn():
    if v.get() == 1:
        print("heiheihei")
filemenu.add_checkbutton(label='heiheihei', variable=v, command=ckbtn)
menubar.add_cascade(label='File', menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label='Undo', command=donothing)
editmenu.add_separator()
cmdlist_for_edit = ['Cut', 'Copy', 'Paste', 'Delete', 'Select All']
for cmd in cmdlist_for_edit:
    editmenu.add_command(label=cmd, command=donothing)
menubar.add_cascade(label='Edit', menu=editmenu)
root.config(menu=menubar)

root.mainloop()
'''
# PaneWindow
'''
import tkinter as tk
root = tk.Tk()
pane = tk.PanedWindow(orient=tk.VERTICAL)
pane.pack(fill=tk.BOTH, expand=1, anchor='w')
for w in [tk.Label, tk.Button, tk.Checkbutton, tk.Radiobutton]:
    pane.add(w(pane, text="hello"))
tk.mainloop()
'''
# Canvas的使用，画图图
'''
import tkinter as tk

root = tk.Tk()
cv = tk.Canvas(root, bg='white')
cv.pack()
rt1 = cv.create_rectangle(10, 10, 110, 110, outline='blue', width=5, fill='red', dash=100, stipple='gray12', tags=('r1', 'r2'))
rt2 = cv.create_rectangle(20, 20, 80, 80, tags='r3')
print(cv.find_withtag('r3'))
# Canvas使用了stack技术，创建item总是位于前一个创建的item之上
cv.addtag_above('r4', rt1)
cv.addtag_below('r5', rt2)
print(cv.gettags(rt1))
print(cv.gettags(rt2))
# 修改与r3标签绑定的item
for item in cv.find_withtag('r5'):
    cv.itemconfig(item, outline='green')
cv.move(rt1, -5, -5)
cv.delete(rt2)
cv.tag_bind('r1', '<Button-1>', lambda event: print('hello'))
cv.coords(rt1, (40, 40, 140, 140))

arc = cv.create_arc(140, 140, 300, 300, start=0, exten=270, fill='red', style=tk.CHORD)

d = {1:'error', 2:'info', 3:'question', 4:'hourglass'}
for i in d:
    cv.create_bitmap((20*i, 20), bitmap=d[i])

cv.create_line(0, 0, 100, 100, arrow='last', arrowshape='40 40 10')
# 多边形
cv.create_polygon(200, 200, 150, 150, 400, 200, fill='green')

cv.create_text(400, 300, text='hello')


tk.mainloop()
'''
# Canvas上创建组件并滚动
'''
import tkinter as tk
import tkinter.ttk as ttk
import time
root = tk.Tk()
cv = tk.Canvas(root, bg='white')
cv.grid(row=0, column=0)
class BtnCreator:
    def __init__(self, seq_num):
        self.seq_num = seq_num
        btn = ttk.Button(cv, text='Btn'+str(self.seq_num), width=10, command=lambda: print("这是第%d个按钮" % self.seq_num))
        cv.create_window((20, 40 * (self.seq_num+1)), window=btn, anchor='w')
def createBtn(seq_num):
    btn = ttk.Button(cv, text='Btn' + str(seq_num), width=10, command=lambda: print("这是第%d个按钮" % seq_num))
    cv.create_window((20, 40 * (seq_num+1)), window=btn, anchor='w')
for i in range(50):
    # BtnCreator(i)
    createBtn(i)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=cv.yview)
cv.config(yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='sen')
scrollbar.bind("<Configure>", lambda event: cv.config(scrollregion=cv.bbox("all")))

tk.mainloop()
'''
# 鼠标右键弹出菜单
'''
import tkinter as tk
root = tk.Tk()
menubar = tk.Menu(root, tearoff=False)
menubar.add_command(label="1")
menubar.add_command(label='2')
frm = tk.Frame(root, width=100, height=100, bg="blue")
frm.pack()
def clickRightKey(event):
    menubar.post(event.x_root, event.y_root)
frm.bind("<Button-3>", clickRightKey)
root.mainloop()
'''

# 多进程：Process，启动一个进程，注意Process必须是在主函数中运行！
'''
from multiprocessing import Process
import os

def run_proc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))

if __name__ == '__main__':
    print("Parent process %s." % os.getpid())
    p = Process(target=run_proc, args=("test", ))
    print("Child process will start.")
    p.start()
    p.join()        # 等待子进程结束后再执行下列代码。 通常用于进程间的同步。
    print("Child process end.")
'''
# subpprocess 运行子进程并读取
'''
import subprocess

file = open("test.txt", 'w')
p = subprocess.Popen(["tasklist"], stdout=subprocess.PIPE)
while(1):
    line = p.stdout.readline()
    if not line:
        break
    print(line)
    file.write(line.decode("gbk"))
print("Exit code: ", p.returncode)
file.close()
'''
# 多线程
'''
import time
import threading

def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)

print("thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target=loop, name="LoopTread")
t.start()
print("the running thread now names %s", threading.current_thread().name)
t.join()
print("thread %s end." % threading.current_thread().name)
'''
# getopt试刀
'''
import sys
import os
import getopt

path = r"F:\python\TestForGetopt"

try:
    opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
except getopt.GetoptError:
    print("Fuck, the program goes wrong")
    os.system("pause")
    exit()

for o, a in opts:
    if o in ("-h", "--help"):
        print("hehe")
    if o in ("-o", "--output"):
        os.system("start "+os.path.join(path, a))

for arg in args:
    print(arg)
'''
# 下 载网页(方法1)
'''
import urllib.request as urllib2
# from bs4 import BeautifulSoup

# 直接请求
try:
    response = urllib2.urlopen("http://oa.haitian.com")
# 获取状态码，如果是200表示获取成功
    print(response.getcode())
# 读取内容
    cont = response.read()
    soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
    links = soup.find_all('a')
    for link in links:
        print(link.name, link['href'], link.get_text)
except:
    print("Scratch the url failed")
'''
# 下载网页(方法2)
'''
import urllib.request as urllib2

# 创建对象
request = urllib2.Request("http://www.baidu.com")
# 添加数据(python3取消了add_data)
# request.add_data('a', '1')
# 添加http的header
request.add_header("User-Agent", "Mozilla/5.0")
# 发送请求
response = urllib2.urlopen(request)
print(response.getcode())
cont = response.read()
print(cont.decode('utf-8'))
'''

# 删除某路径下所有文件/文件夹
'''
import os

tempdir = r'F:\python\测试文件'

if os.path.exists(tempdir):
    for root, dirs, files in os.walk(tempdir, False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
'''
# 修改文本内容
'''
import re
import subprocess

path = r"F:\python\TestFile\testfile.txt"

try:
    fp = open(path, 'r+')
except:
    print("The file was not existed!\nA new test file has been created")
    fp = open(path, 'w+')
    fp.write("Account:\t\nPassword:\t\nCreatedDate:\t\n")
    fp.seek(0)
# s = fp.read()
lines = fp.readlines()
fp.close()
# print("The new-created test file is: \n")
# print(s)
# a = s.split('\n')

pos_of_insert = 0
for line in lines:
    if "Account" in line:
        break
    else:
        pos_of_insert += 1

# a[pos_of_insert] = "Account:\t360849048"
lines[pos_of_insert] = "Account:\t360849048\n"
# s = '\n'.join(a)
fp = open(path, 'w+')
# fp.write(s)
for line in lines:
    fp.write(line)
fp.close()

subprocess.Popen(' '.join(["notepad.exe", path]))
'''
'''
import os
import shutil

path = r"F:\python\名单"
file = r"F:\python\名单\样本.txt"

if not os.path.exists(os.path.join(path, "1.txt")):
    # 如果尚未生成名单，则拷贝100份样本文件，并分别命名为1.txt到100.txt
    for name in range(1, 101):
        shutil.copyfile(file, os.path.join(path, str(name)+'.txt'))

pos_of_line = 0
if os.path.isdir(path):
    for file in os.listdir(path):
        pos_of_line = 0
        fp = open(os.path.join(path, file), 'r')
        lines = fp.readlines()
        for line in lines:
            if line.startswith("No"):
                lines[pos_of_line] = "No: " + os.path.splitext(file)[0]+'\n'
                break
            pos_of_line += 1
        fp.close()
        fp = open(os.path.join(path, file), 'w')
        for line in lines:
            fp.write(line)
        fp.close()
'''
# 将目录下的所有文件夹名字按创建时间降序输出到txt文本
'''
import os
import subprocess

path = r"E:\订单制作"
filename = r"订单号.txt"

dirs = []
fp = open(os.path.join(path, filename), "w")
for file in os.listdir(path):
    if os.path.isdir(os.path.join(path, file)):
        dirs.append(file)

def getBuiltTime(file, path=path):
    return os.stat(os.path.join(path, file)).st_ctime

dirs = sorted(dirs, key=getBuiltTime, reverse=True)
i = 0
for file in dirs:
    i += 1
    fp.write("{0}------>{1}\n".format('%2d'%i, file))
print("一共找到并导出了%d个文件夹名" % i)
fp.close()
subprocess.Popen(os.path.join(path, filename), shell=True)
'''
# ttk.Progressbar的使用
'''
import tkinter as tk
import os
import threading

from tkinter import *
from tkinter import ttk
import time


def manu_increment(*args):
    for i in range(100):
        p1["value"] = i + 1
        root.update()
        time.sleep(0.1)


def auto_increment(*args):
    global flag, value
    flag = not flag

    if flag:
        btn2["text"] = "暂停动画"
        p2.start(10)
    else:
        btn2["text"] = "开始动画"
        value = p2["value"]
        p2.stop()
        p2["value"] = value


root = Tk()
root.title("Progressbar组件")
# 定量进度条
p1 = ttk.Progressbar(root, length=200, mode="determinate", orient=HORIZONTAL)
p1.grid(row=1, column=1)
p1["maximum"] = 100
p1["value"] = 0

# 通过指定变量，改变进度条位置
# n = IntVar()
# p1["variable"] = n

# 通过指定步长，改变进度条位置
# p1.step(2)

btn = ttk.Button(root, text="开始动画", command=manu_increment)
btn.grid(row=1, column=0)

# 非定量进度条
flag = False  # 标志位
value = 0  # 进度条位置

p2 = ttk.Progressbar(root, length=200, mode="indeterminate", orient=HORIZONTAL)
p2.grid(row=2, column=1)

btn2 = ttk.Button(root, text="自动动画", command=auto_increment)
btn2.grid(row=2, column=0)

root.mainloop()
'''

# sqlite3的基本用法
'''
import sqlite3
import os

path_db = os.path.join(os.getcwd(), 'test.db')

# sqlite3连接数据库，没有则新建一个数据库
conn = sqlite3.connect(path_db)
print("Opened/Created database successfully")
conn.close()

# 在数据库中创建一个表
conn = sqlite3.connect(path_db)
try:
    conn.execute('CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL);')
    print("Table created successfully")
except:
    print("表COMPANY已经存在，不能重复创建表")
conn.close()

# 在已创建的表中创建记录
conn = sqlite3.connect(path_db)
try:
    conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (5, 'Paul', 32, 'California', 20000.00)")
    conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (6, 'Allen', 25, 'Texas', 15000.00)")
    conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (7, 'Teddy', 23, 'Norway', 20000.00)")
    conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (8, 'Mark', 23, 'Rich-Mond', 65000.00)")
    conn.commit()
    print("Records created successfully")
except:
    print("表中数据不可重复")
conn.close()

# 从表中获取并显示数据
conn = sqlite3.connect(path_db)
# cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
cursor = conn.execute("SELECT ID, NAME, ADDRESS, SALARY from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], '\n')
print("Operation done successfully")
conn.close()

# 更新表中的数据
conn = sqlite3.connect(path_db)
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit()
print("Total number of rows updated: ", conn.total_changes)
conn.close()

# 删除表中的数据
conn = sqlite3.connect(path_db)
conn.execute("DELETE from COMPANY where ID=4")
conn.commit()
print("Total number of rows deleted: ", conn.total_changes)
conn.close()

import sqlite3
import codecs

path_db = r'E:\ZhaFir\swg\Database\Language\Languages.db'
path_txt = r'E:\ZhaFir\swg\Database\Language\Languages.csv'

fp = codecs.open(path_txt, 'w', 'utf-8')
conn = sqlite3.connect(path_db)
cursor = conn.execute("select * from Texts_Table;")
print(type(cursor))
for row in cursor:
    for i in row:
        fp.write(str(i))
        fp.write(',')
    fp.write('\n')
fp.close()
conn.close()
'''

# 为scrollbar绑定鼠标滚轮事件
'''
import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.frm = tk.LabelFrame(self.root)
        self.frm.grid()
        self.__createText()

        tk.mainloop()

    def __createText(self):
        text = tk.Text(self.frm, width=30, height=40, bg='white')
        text.grid(row=0, column=0)
        scrollbar = ttk.Scrollbar(self.frm, orient=tk.VERTICAL, command=text.yview)
        text.config(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='sn')
        for i in range(100):
            text.insert("end", i)
            text.insert('end', '\n')
        def scrollMouseWheel(event):
            text.yview_scroll(-1*(event.delta//120), 'units')
        scrollbar.bind("<MouseWheel>", scrollMouseWheel)


app = App()

'''
# 为canvas增加鼠标滚轮事件
'''
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
cv = tk.Canvas(root, bg='white')
cv.grid()

def createBtn(seq_num):
    btn = ttk.Button(cv, text='Button'+str(seq_num+1), width=10, command=lambda: print("%d" % (seq_num+1)))
    cv.create_window((20, 40*(seq_num+1)), window=btn, anchor='w')
for i in range(50):
    createBtn(i)
# slb = ttk.Scrollbar(root, orient=tk.VERTICAL, command=cv.yview)
# cv.config(yscrollcommand=slb.set)
# slb.grid(row=0, column=1, sticky='wsn')
cv.bind("<Configure>", lambda event: cv.config(scrollregion=cv.bbox("all")))

def scrollMouse(event):
    cv.yview_scroll(-1*(event.delta//120), 'pages')
cv.bind("<MouseWheel>", scrollMouse)

tk.mainloop()
'''

# 利用socket连接网站
'''
import socket

# 创建一个socket，AF_INET指定使用IPv4，如果需要IPv6，则为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.baidu.com', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
print(data)
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)
'''
# 支持多线程的服务器程序
'''
import socket
import threading
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('172.18.71.158', 9999))
serversocket.listen(5)
def tcplink(clientsocket, addr):
    print('Accept new connect from % s: % s…' % addr)
    clientsocket.send(b'Welcome')
    while True:
        data = clientsocket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        clientsocket.send(('Hello, % s' % data.decode('utf-8')).encode('utf-8'))
    clientsocket.close()
    print('Connection from % s: % s closed' % addr)

while True:
    clientsocket, addr = serversocket.accept()
    t = threading.Thread(target=tcplink, args=(clientsocket, addr))
    t.start()
'''
# 测试客户端给服务器停止命令（未成功）
'''
import socket
import sys
import threading

HOST = ''
PORT = 8888

serRun = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
try:
    s.bind((HOST, PORT))
except:
    print("Bind failed")
    sys.exit()
print("Socket bind complete")

s.listen(5)
print("Socket now listening")

def clientthread(conn, addr):
    global serRun
    conn.send(b"Welcome to the server. Type something and hit enter\n")
    while True:
        data = conn.recv(1024)
        reply = 'OK....' + data.decode("utf8")
        if not data or data.decode('utf-8') == 'exit':
            break
        conn.sendall(reply.encode("utf-8"))
        if data.decode("utf8") == "stop server":
            print("The server stoped")
            serRun = False
            exit()
    conn.send(b"The connection closed!")
    conn.close()
    print('Connection %s: %s has closed!', addr)

while serRun:
    # 程序会堵在accept()，因此无法检测serRun
    conn, addr = s.accept()
    print("Connection %s: %s has been created!", addr)
    threading._start_new_thread(clientthread, (conn, addr))

s.close()
print("Server stoped")
'''

# 客户端程序
'''
import socket
import pickle
import time

clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clt.connect(("127.0.0.1", 9999))
clt.send(b"all")
result = []
i = 0
while True:
    stream = clt.recv(1024)
    if not stream:
        i += 1
    try:
        temp = pickle.loads(stream)
        if temp == "__Done__...":
            clt.close()
            break
        result.append(temp)
    except:
        pass
    if i >= 10:
        break
for i in result:
    print(i)
'''

# excel操作
'''
import xlrd

# 打开工作簿
workbook = xlrd.open_workbook(r"F:\python\软件版本登记表.xls")
# 获得所有工作表名
sheet_names = workbook.sheet_names()
print("工作簿中表如下：\n", sheet_names)
sheets = workbook.sheets()
print(sheets)

print("*"*70 + "下面对某一个表进行读取" +"*"*70)

# 通过工作表名字进入工作表
sheet = workbook.sheet_by_name(sheet_names[4])
# 通过index进入工作表
# sheet = workbook.sheet_by_index(4)

# 获取工作表的名字，行数，列数
print("表明：%s\n" % sheet.name, "行数：%s\n" % sheet.nrows, "列数：%s" % sheet.ncols)
# 获取工作表内某一行的内容
print("获取第一行前8项：" , sheet.row_values(0)[:8])
# 获取某一列的内容
print("获取第一列前8项：" , sheet.col_values(0)[:8])
'''

# 解析客户端语句
'''
def parseAndExec(t_soft, msg):
    obj, name, args = msg
    arg1 = []
    arg2 = None
    for arg in args:
        if isinstance(arg, dict):
            arg2 = arg
        else:
            arg1.append(arg)
    if obj == "a":
        if arg1 != [] and arg2 != None:
            getattr(t_soft, name)(*arg1, **arg2)
        elif arg1 != [] and arg2 == None:
            getattr(t_soft, name)(*arg1)
        elif arg1 == [] and arg2 != None:
            getattr(t_soft, name)(**arg2)
        else:
            getattr(t_soft, name)


class A:
    def Ma(self, a):
        print(a)

    def Mb(self, **kv):
        for k,v in kv.items():
            print(k, v)

a = A()
parseAndExec(a, ('a', 'Mb', ({'a':1, 'b':2}, )))
'''

# 使用WSGI进行接收http请求和发送http响应
'''
from wsgiref.simple_server import make_server
def app(environ, response):
    print("Method: " + environ["REQUEST_METHOD"])
    print("Path: " + environ["PATH_INFO"])
    response("200 OK", [("Content-Type", "text/html")])
    return [b'<h1>Halo</h1>']
httpd = make_server('', 8899, app)
httpd.serve_forever()
'''
'''使用flask模块进行简单处理'''
# from flask import Flask
# from flask import request
# from flask import render_template
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '''<h1>This is the home page</h1>
#               <form action="/signin">
#                   <button type="submit">Sign in</button>
#               </from>
#     '''
#
# @app.route('/signin', methods=['GET'])
# def siginin_form():
#     return '''<form action="/signin", method="post">
#                   <input type="text" name="username" placeholder="Account">
#                   <input type="password" name="password" placeholder="xxx">
#                   <button type="submit">Sign in</button>
#               </form>
#               <form action="/", method="get">
#                   <button type="submit">Back homepage</button>
#               </form>
#               '''
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     if request.form['username'] == 'admin' and request.form['password'] == 'admin':
#         return '<h3>Halo, %s</h3>' % request.form['username']
#     return '<h3>Bad username or password.</h3>'
#
# @app.route('/hello/<name>', methods=['GET'])
# def sayHi(name):
#     return "Hello %s" % name
#
# @app.route('/test', methods=['GET'])
# def enterTestPage():
#     return render_template("flex.html")
#
# @app.route('/test-<name>', methods=['GET'])
# def usingTemplate(name):
#     return render_template("flex.html", name=name)
#
#
# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=9999)

# 使用urllib进行网页访问

# 使用urllib进行GET请求
'''
from urllib import request
import codecs

req = request.Request("http://www.baidu.com")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
resp = request.urlopen(req)
html = resp.read().decode()

fp = codecs.open("baidu.html", 'w+', 'utf-8')
for line in html:
    fp.write(line)
fp.close()
'''

'''爬取普通话成绩'''
#
# from urllib import request, parse
# from bs4 import BeautifulSoup
# import codecs
# import threading
# import time
#
# num = 1
# fp = codecs.open(r"D:\Users\J\Desktop\2017.csv", "w+")
# first_zkzh = '02017112500001'
#
# while num < 440:
#
#     if num > 99:
#         # zkzh = '3302016160' + str(num)
#         zkzh = first_zkzh[:-3] + str(num)
#     elif num > 9:
#         # zkzh = '33020161600' + str(num)
#         zkzh = first_zkzh[:-2] + str(num)
#     else:
#         # zkzh = '330201616000' + str(num)
#         zkzh = first_zkzh[:-1] + str(num)
#     num += 1
#     query_data = parse.urlencode([
#         ('zkzh', zkzh)
#     ])
#     req = request.Request('http://cjcx.nbedu.net.cn/querypth101101.asp')
#     req.add_header('Origin', 'http://cjcx.nbedu.net.cn')
#     req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
#     try:
#         with request.urlopen(req, data=query_data.encode('utf-8'), timeout=5) as f:
#             # print('Status:', f.status, f.reason)
#             for k, v in f.getheaders():
#                 # print('%s: %s' % (k, v))
#                 pass
#             html_doc = f.read().decode('gbk')
#     except:
#         print(zkzh, 'time out!')
#         continue
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     # print(soup.prettify())
#     tags = soup.find_all("td", {"class": "default_small_font"})
#     if not tags:
#         print(zkzh, 'not find')
#         continue
#     for tag in tags:
#         # print(tag.get_text())
#         fp.write(tag.get_text())
#         fp.write(',')
#     fp.write('\n')
# fp.close()

'''使用闭包'''
# def countGe(start_num):
#     def count():
#         nonlocal start_num
#         start_num += 1
#         return start_num
#     return count
#
# count = countGe(0)
# print(count())
# print(count())
# print(count())
'''循环队列'''
#
# Python有自带队列的方法 from collections import deque
#
# import time
# import threading
#
# class Queue:
#     def __init__(self, queue_length):
#         self.queue = []
#         self.queue_len = queue_length
#         # 头部指针，指向当前数据
#         self.present_work_pointer = 0
#         # 尾部指针，指向最后数据
#         self.top_work_pointer = 0
#         # 是否是第一次循环，因为首次需用append方法增加队列长度
#         self.first_circle = True
#         # 头部指针是否已经进入下一循环追赶头部指针，
#         # 尾部指针从队列末尾到队列头部时，该变量改为True，
#         # 头部指针从队列尾部到队列头部时，该变量改为False。
#         self.reverse = False
#
#     # func:   入列
#     # retval: True  成功
#     #         False 队列溢出
#     def push(self, anything):
#         # 尾部指针首次循环，使用append增加长度，不存在追赶的情况
#         if self.first_circle:
#             self.queue.append(anything)
#             self.top_work_pointer += 1
#             # 尾部指针超出队列时，尾部指针归零
#             if self.top_work_pointer >= self.queue_len:
#                 self.first_circle = False
#                 self.top_work_pointer = 0
#                 self.reverse = True
#         else:
#             # 尾部指针和头部指针处于统一循环内，不存在追赶的情况时：
#             if not self.reverse:
#                 self.queue[self.top_work_pointer] = anything
#                 self.top_work_pointer += 1
#                 # 尾部指针超出栈高度时，尾部指针归零
#                 if self.top_work_pointer >= self.queue_len:
#                     self.top_work_pointer = 0
#                     self.reverse = True
#             else:
#                 # 尾部指针赶上了头部指针，禁止写入
#                 if self.top_work_pointer >= self.present_work_pointer:
#                     return False
#                 self.queue[self.top_work_pointer] = anything
#                 self.top_work_pointer += 1
#         return True
#
#     # func:   出列
#     # retval: 获得当前头部指针所指向的内容，如果是None代表当前队列已经没有任何东西
#     def pop(self):
#         retval = None
#         # 队列内没有任何内容
#         if (self.top_work_pointer - self.present_work_pointer) == 0 and not self.reverse:
#             return retval
#         retval = self.queue[self.present_work_pointer]
#         self.present_work_pointer += 1
#         # 如果头部指针到达队列尾部，头部指针清零
#         if self.present_work_pointer >= self.queue_len:
#             self.present_work_pointer = 0
#             self.reverse = False
#         return retval
#
# # 下面用两条线程模拟入列和出列
# stack = Queue(5)
# def push_every1s():
#     for i in range(20):
#         if not stack.push(i):
#             print("*队列溢出: " + str(i) + '*')
#         else:
#             print("*入列: " + str(i) + '*')
#         time.sleep(1)
# def pop_every2s():
#     for i in range(20):
#         print(stack.pop())
#         time.sleep(2)
#
# t1 = threading.Thread(target=push_every1s, args=())
# t2 = threading.Thread(target=pop_every2s, args=())
# t1.start()
# t2.start()

'''
使用openpyxl读写excel.xlsx文件
'''
# import os
# import openpyxl
#
# path = r'F:\python\excel'
# filename1 = r'openpyxl-demo.xlsx'
# filename2 = r'dup-openpyxl-demo.xlsx'
#
# wb = openpyxl.Workbook()
# ws2 = wb.create_sheet('Sec')
# ws1 = wb.active
# ws1.title = "Fir"
# ws1.sheet_properties.tabColor = '1072BA'
#
# # 单元格写入
# # 使用  ws1['a1'] = xxx  或者  ws1.cell(1, 1).value = xxx  进行单元格赋值
# for i in range(1, 101):
#     ws1['A'+str(i)] = i
#     ws1['b'+str(i)] = i+1
#     ws1['c' + str(i)] = i + 2
#
# # 获取一片单元格数据并遍历读取
# # 使用 ws1['a1':'c4'] 选中某一片单元格
# # 使用ws.rows或ws.columns选中所有单元格
# for row in ws1['a1':'c100']:
#     for cell in row:
#         print(cell.value)
#
# # 保存单元格，生成xlsx文件
# pathname1 = os.path.join(path, filename1)
# wb.save(pathname1)
#
# # 加载刚保存的文件，修改并另存为
# pathname2 = os.path.join(path, filename2)
# wb2 = openpyxl.load_workbook(pathname1)
# ws1 = wb2[wb2.sheetnames[0]]
# for row in ws1.rows:
#     for cell in row:
#         cell.value = 1
#
# wb2.save(pathname2)

'''
使用openpyxl进行excel样式操作
'''
# import openpyxl
# import os
#
# path = r'F:\python\excel'
# filename1 = r'openpyxl-demo.xlsx'
# pathname = os.path.join(path, filename1)
#
# wb = openpyxl.Workbook()
# sheet0 = wb.active
# sheet0.merge_cells('a1:b2')
# sheet0['a1'] = 'heelo world'
#
# wb.save(pathname)

''' POST请求 '''
from urllib import request, parse


# url = 'http://192.168.100.179/HTMSOFT/login.aspx'
# data = {'tbUserName': '符杰',
#         'tbPassword': '123',
#         'btnLogin.x': '0',
#         'btnLogin.y': '0',
#         '__VIEWSTATE': '/wEPDwUJNTgyMTgzOTAwZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUIYnRuTG9naW6+uccHMrC9W3Fj9V19pTtYEUP+FQ==',
#         '__EVENTVALIDATION': '/wEWBALBgfSYBALyj/OQAgKC3IeGDAK3jsrkBCS71u5ccex1QMH1jZ1NNhyYJAJN'
# }
url = 'http://127.0.0.1:5000/createconfigfile'
data = {
{"boardModules1":["","","",""],"boardModules2":["","","",""],"boardModules3":["","","",""],"boardModulesIOs1":['{}','{}','{}','{}'],"boardModulesIOs2":['{}','{}','{}','{}'],"boardModulesIOs3":['{}','{}','{}','{}'],"varanConnModulePos":0,"evaluationNum":"","productionNum":"","immType":"ve400-80","customer":"","safetyStandard":"","technicalClause":"","designNote":"","funcConfig":{"1":{"name":"功能点1注射信号","status":False},"2":{"name":"功能点2储料信号","status":False},"3":{"name":"E73","status":False},"4":{"name":"喷嘴改阀门1","status":False},"5":{"name":"DEE能耗模块","status":False},"6":{"name":"7号改可编程","status":False},"7":{"name":"阀门","status":False},"8":{"name":"吹气","status":False},"9":{"name":"中子","status":False},"10":{"name":"可编程IO","status":False},"666":{"name":"外置热流道","status":False}},"pilzNor":"","pilzE73":"","extHotrunnerNum":3,"intHotrunnerNum":0,"isBigImm":False,"isDualInj":False,"clampForce":"400","injection":"80","type":"VE2","ceStandard":False}
}
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Content-Length': 294,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': '192.168.100.179',
    'Origin': 'http://192.168.100.179',
    'Refer': 'http://192.168.100.179/HTMSOFT/login.aspx',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

data = parse.urlencode(data).encode()
req = request.Request(url=url, data=data, headers=header)
page = request.urlopen(req).read()
print(dir(req))
print(req.get_method())
print(page.decode())

'''POST JSON数据的方式'''
# 首先对data进行转码，转化成str类型
data = urllib.parse.urlencode(data) 
#  post请求只支持byte类型，所以要进行再次编码
data = data.encode('utf-8')  
 # 对url和参数进行包装
new_url = urllib.request.Request(url,data) 
response = urllib.request.urlopen(new_url) 
# 读取响应结果
response = result.read() 
#  对响应结果解码
print(response.decode("utf8"))



