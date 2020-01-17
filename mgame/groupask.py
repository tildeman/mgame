import tkinter
def nofg():
    global t,gl,ng,sp,sm
    t=tkinter.Tk()
    gl=tkinter.Label(t,text='How many groups are there in the game?',font=('Arial',15))
    gl.pack()
    ng=tkinter.IntVar()
    sp=tkinter.Spinbox(t,from_=2,to=20,width=50,font=('Arial',10),textvariable=ng)
    sp.pack()
    sm=tkinter.Button(width=50,text='OK',font=('Arial',10),command=lambda:t.destroy())
    sm.pack()
    t.mainloop()
    
