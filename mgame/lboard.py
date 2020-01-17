import tkinter
def mboard(a):
    t=tkinter.Tk()
    l=tkinter.Label(font=('Arial',20),text='Leaderboard')
    l.pack()
    s=tkinter.Scrollbar(t)
    s.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    f=tkinter.Listbox(t,relief=tkinter.SUNKEN,yscrollcommand=s.set,font=('Arial',10))
    for n,ss in a:
        f.insert(tkinter.END,n+': '+str(ss))
    f.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
    s.config(command=f.yview)
    t.mainloop()
if __name__=='__main__':
    mboard([('123',1),('321',2),('a',3),('aa',3),('aaa',3),('aaaa',3),('aaaaa',3)])
