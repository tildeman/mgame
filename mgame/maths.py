import groupask
import groupnames
import questiongen
import qcount
import lboard
from collections import Counter as counter
groupask.nofg()
n=groupask.ng.get()
groupnames.names(n)
namelist=groupnames.r
score=counter(dict(zip(namelist,[0]*len(namelist))))
print(score)
for q,a1,a2,a3,a4,cans in questiongen.q:
    qcount.ask(q,a1,a2,a3,a4,cans,namelist)
    n=qcount.res
    if n==0:
        break
    score[n[0]]+=n[1]
lboard.mboard(score.most_common())
