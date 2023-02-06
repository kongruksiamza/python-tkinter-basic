from tkinter import *
#สร้างหน้าจอ
root = Tk() 
#ตั้งค่าหน้าจอ
root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)
root.config(bg="blue")

btn1=Button(root,text="ปุ่มที่ 1")
btn2=Button(root,text="ปุ่มที่ 2")
btn3=Button(root,text="ปุ่มที่ 3")
btn4=Button(root,text="ปุ่มที่ 4")
btn5=Button(root,text="ปุ่มที่ 5")
btn6=Button(root,text="ปุ่มที่ 6")

btn1.grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=10)
btn2.grid(row=0,column=1,padx=5,pady=5,ipadx=10,ipady=10)
btn3.grid(row=0,column=2,padx=5,pady=5,ipadx=10,ipady=10)

btn4.grid(row=1,column=0,padx=5,pady=5,ipadx=10,ipady=10)
btn5.grid(row=1,column=1,padx=5,pady=5,ipadx=10,ipady=10)
btn6.grid(row=1,column=2,padx=5,pady=5,ipadx=10,ipady=10)

root.mainloop()