from tkinter import *
from PIL import ImageTk , Image
#สร้างหน้าจอ
root = Tk() 
#ตั้งค่าหน้าจอ
root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)

#อ่านภาพ
img1=ImageTk.PhotoImage(Image.open("Image/programmer.png"))
Label(root,image=img1).pack()

root.mainloop()