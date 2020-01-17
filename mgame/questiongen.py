from random import randrange,shuffle,choice
from decimal import Decimal as dc
def prod(a):
    if len(a)==0: return 1
    return a[0]*prod(a[1:])
def dquot(a):
    if len(a)==0: return 1
    return a[0]//prod(a[1:])
# +-(1-10) +-(10**) +-(1-1000000000) +++ --- */(1-10) */(10**) */(0.1**) ***/// 
def addsub110():
    def add():
        o=randrange(1,11)
        t=randrange(1,11)
        n=[abs(o-t),o*t//2,randrange(1,11),o+t]
        shuffle(n)
        r=[str(o)+'+'+str(t)+'=?']+n+[o+t]
        return tuple(r)
    def subtract():
        o=randrange(1,11)
        t=randrange(1,o+1)
        n=[o+t,o*t//2,randrange(1,11),o-t]
        shuffle(n)
        r=[str(o)+'-'+str(t)+'=?']+n+[o-t]
        return tuple(r)
    return choice([add,subtract])()
def addsubtp():
    def add():
        p=10**randrange(0,10)
        o=randrange(1,10)*p
        t=randrange(1,10)*p
        n=[abs(o-t),o*t//2,randrange(1,11),o+t]
        shuffle(n)
        r=[str(o)+'+'+str(t)+'=?']+n+[o+t]
        return tuple(r)
    def subtract():
        p=10**randrange(0,10)
        o=randrange(0,10)
        t=randrange(0,o+1)*p
        o*=p
        n=[o+t,o*t//2,randrange(1,11),o-t]
        shuffle(n)
        r=[str(o)+'-'+str(t)+'=?']+n+[o-t]
        return tuple(r)
    return choice([add,subtract])()
def madd():
    n=[randrange(1,101) for x in range(randrange(3,11))]
    r=[sum([n[randrange(len(n))] for y in range(len(n))]) for x in range(3)]+[sum(n)]
    shuffle(r)
    return tuple(['+'.join(map(str,n))+'=?']+r+[sum(n)])
def msub():
    p=randrange(500,1001)
    n=[p]+[randrange(1,101) for x in range(randrange(2,10))]
    r=[p-sum([n[1+randrange(len(n)-1)] for y in range(len(n)-1)]) for x in range(3)]+[n[0]-sum(n[1:])]
    shuffle(r)
    return tuple(['-'.join(map(str,n))+'=?']+r+[n[0]-sum(n[1:])])
def addsub11g():
    def add():
        o=randrange(1,1000000001)
        t=randrange(1,1000000001)
        n=[abs(o-t),o*t//2,randrange(1,1000000001),o+t]
        shuffle(n)
        r=[str(o)+'+'+str(t)+'=?']+n+[o+t]
        return tuple(r)
    def subtract():
        o=randrange(1,1000000001)
        t=randrange(1,o+1)
        n=[o+t,o*t//2,randrange(1,1000000001),o-t]
        shuffle(n)
        r=[str(o)+'-'+str(t)+'=?']+n+[o-t]
        return tuple(r)
    return choice([add,subtract])()
def muldiv110():
    def multiply():
        o=randrange(1,11)
        t=randrange(1,11)
        n=[abs(o-t),o+t//2,randrange(1,11),o*t]
        shuffle(n)
        r=[str(o)+'*'+str(t)+'=?']+n+[o*t]
        return tuple(r)
    def divide():
        t=randrange(1,11)
        o=randrange(1,11)*t
        n=[o%t,o*t//2,randrange(1,11),o//t]
        shuffle(n)
        r=[str(o)+'/'+str(t)+'=?']+n+[o//t]
        return tuple(r)
    return choice([multiply,divide])()
def muldivtp():
    def multiply():
        p=10**randrange(0,10)
        o=randrange(1,10)*p//(10**randrange(0,10))
        t=randrange(1,10)*p
        n=[abs(o-t),o+t//2,randrange(1,11),o*t]
        shuffle(n)
        r=[str(o)+'*'+str(t)+'=?']+n+[o*t]
        return tuple(r)
    def divide():
        p=randrange(1,10)
        pt=10**randrange(1,p+1)
        p=10**p
        t=randrange(1,10)
        o=randrange(0,10)*t
        t*=pt
        o*=p
        n=[o%t,o*t//2,randrange(1,11),o//t]
        shuffle(n)
        r=[str(o)+'/'+str(t)+'=?']+n+[o//t]
        return tuple(r)
    return choice([multiply,divide])()
def muldiv11g():
    def multiply():
        o=randrange(1,1000000001)
        t=randrange(1,1000000001)
        n=[abs(o-t),o+t//2,randrange(1,1000000001),o*t]
        shuffle(n)
        r=[str(o)+'*'+str(t)+'=?']+n+[o*t]
        return tuple(r)
    def divide():
        t=randrange(1,1000000001)
        o=randrange(1,1000000001)*t
        n=[o%t,o*t//2,randrange(1,1000000001),o//t]
        shuffle(n)
        r=[str(o)+'/'+str(t)+'=?']+n+[o//t]
        return tuple(r)
    return choice([multiply,divide])()
def mmul():
    n=[randrange(1,11) for x in range(randrange(3,11))]
    r=[prod([n[randrange(len(n))] for y in range(len(n))]) for x in range(3)]+[prod(n)]
    shuffle(r)
    return tuple(['*'.join(map(str,n))+'=?']+r+[prod(n)])
def mdiv():
    n=[randrange(1,11) for x in range(randrange(3,10))]
    px=prod(n)*randrange(1,11)
    n=[px]+n
    r=[n[randrange(1,len(n))] for x in range(3)]+[dquot(n)]
    shuffle(r)
    return tuple(['/'.join(map(str,n))+'=?']+r+[dquot(n)])
q=[addsub110(),addsubtp(),madd(),msub(),addsub11g(),muldiv110(),muldivtp(),muldiv11g(),mmul(),mdiv()]
