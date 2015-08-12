from Tkinter import *
from math import *
class App:
	def __init__(self,master):
		frame=Frame(master,bg="White",padx=100,pady=100)
		frame.master.title("CALCULATOR")
		frame.pack()
		entry1=Entry(frame,bg="Pink",)
		entry1.grid(row=0,pady=5)
		ans1=Entry(frame,bg="Green")
		ans1.grid(row=0,column=1)
		def simpl():
			ans1.delete(0,END)
			cal1=eval(entry1.get())
			ans1.insert(0,"=")
			ans1.insert(1,cal1)
		def root():
			ans1.delete(0,END)
			ans1.insert(0,"Root(")
			cal2=sqrt(int(eval(entry1.get())))
			ans1.insert(5,eval(entry1.get()))
			ans1.insert(len(entry1.get())+5,")=")
			ans1.insert(len(entry1.get())+7,cal2)
		def square():
			ans1.delete(0,END)
			ans1.insert(0,"Square(")
			cal6=int(eval(entry1.get()))**2
			ans1.insert(7,eval(entry1.get()))
			ans1.insert(len(entry1.get())+7,")=")
			ans1.insert(len(entry1.get())+9,cal6)
		def sine():
			ans1.delete(0,END)
			ans1.insert(0,"Sin(")
			cal3=sin(radians(int(eval(entry1.get()))))
			ans1.insert(4,eval(entry1.get()))
			ans1.insert(len(entry1.get())+4,")=")
			ans1.insert(len(entry1.get())+6,cal3)
		def cose():
			ans1.delete(0,END)
			ans1.insert(0,"Cos(")
			cal4=cos(radians(int(eval(entry1.get()))))
			ans1.insert(4,eval(entry1.get()))
			ans1.insert(len(entry1.get())+4,")=")
			ans1.insert(len(entry1.get())+6,cal4)
		def tane():
			ans1.delete(0,END)
			ans1.insert(0,"Tan(")
			cal5=tan(radians(int(eval(entry1.get()))))
			ans1.insert(4,eval(entry1.get()))
			ans1.insert(len(entry1.get())+4,")=")
			ans1.insert(len(entry1.get())+6,cal5)
		def clear():
			ans1.delete(0,END)
			entry1.delete(0,END)
		butt=Button(frame,text="' Eval  '",bg="Pink",fg="Blue",command=simpl )
		butt.grid(row=1,column=0)
		d1={"' Root '":root,"Square":square}
		i=2
		for k,v in d1.items():
			butt2=Button(frame,text=k,fg="Blue",bg="Pink",command=v )
			butt2.grid(row=i,column=0)
			i+=1
		d2={"'   Sin  '":sine,"'  Cos  '":cose,"'  Tan  '":tane}
		i=1
		for k,v in d2.items():
			butt2=Button(frame,text=k,fg="Blue",bg="Pink",command=v )
			butt2.grid(row=i,column=1)
			i+=1
		butt1=Button(frame,text="' Clear '",bg="Pink",fg="Blue",command=clear )
		butt1.grid(row=5,column=0)
		butt3=Button(frame,text="' Close '",bg="Pink",fg="Blue",command=frame.quit )
		butt3.grid(row=5,column=1)
root=Tk()
im=PhotoImage(file="varun.gif")#Change the picture here
label=Label(root,image=im,padx=1,pady=1,bg="White")
label.pack(fill="both",expand="yes")
app=App(root)
root.mainloop()
