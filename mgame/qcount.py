import tkinter
from time import sleep
def ask(q,a1,a2,a3,a4,cans,gs):
    global res
    res=0
    t=tkinter.Tk()
    l=tkinter.Label(t,text=q,font=('Arial',40))
    l.pack()
    m1=tkinter.Label(t,text='Group:')
    m1.pack()
    g=tkinter.Frame()
    g.pack()
    m1=tkinter.Label(t,text='Answered first with answer:')
    m1.pack()
    f=tkinter.Frame()
    f.pack()
    gb=[]
    gn=tkinter.StringVar()
    an=tkinter.IntVar()
    def cscore():
        if gn.get()=='':
            le=tkinter.Label(t,text='Umm... Which group does the answer belong to?',font=('Arial',10),fg='#ff0000')
            le.pack()
            t.update()
            sleep(1)
            le.destroy()
            return
        if an.get()==cans:
            for x in fa:
                if x.config()['value'][-1]==an.get():
                    n=x.config()['fg']
                    x.config(fg='#008000')
                    t.update()
                    sleep(1)
                    x.config(fg='#000000')
                    break
        else:
            for x in fa:
                if x.config()['value'][-1]==an.get():
                    n=x.config()['fg']
                    x.config(fg='#ff0000')
                    t.update()
                    sleep(1)
                    x.config(fg='#000000')
                    break
        global res
        res=(gn.get(),an.get()==cans)
        t.destroy()
    for x in gs:
        gb.append(tkinter.Radiobutton(g,text=x,variable=gn,value=x,indicatoron=0,font=('Arial',10),width=82//len(gs)))
        gb[-1].pack(side=tkinter.LEFT)
    fa=[]
    for x in [a1,a2,a3,a4]:
        fa.append(tkinter.Radiobutton(f,indicatoron=0,value=x,text=str(x),font=('Arial',10),width=20,command=cscore,variable=an))
        fa[-1].pack(side=tkinter.LEFT)
    t.mainloop()
if __name__=='__main__':
    ask('Test question',1,2,3,4,4,['Group A','Group B'])
