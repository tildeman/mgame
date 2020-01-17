import tkinter
from time import sleep
def names(n):
    global t,f,nl,b
    t=tkinter.Tk()
    f=[]
    nl=tkinter.Label(t,text='Team names?',font=('Arial',15))
    nl.pack()
    for x in range(n):
        f.append(tkinter.Entry(t,width=50,font=('Arial',20)))
        f[-1].pack()
    def destroy():
        global t,r
        r=[x.get() for x in f]
        for x in range(len(r)):
            if r[x] in r[:x]+r[x+1:]:
                wl=tkinter.Label(text='Duplicates! Look again, team names.',fg='#ff0000',font='Arial')
                wl.pack()
                t.update()
                sleep(2)
                wl.destroy()
                return
        if '' in r:
            wl=tkinter.Label(text='So nameless! Check your team, name.',fg='#ff0000',font='Arial')
            wl.pack()
            t.update()
            sleep(2)
            wl.destroy()
            return
        t.destroy()
    b=tkinter.Button(t,text='OK',command=destroy)
    b.pack()
    t.mainloop()
