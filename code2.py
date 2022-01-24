from random import randrange
from collections import Counter
import sys

ulist=[]
vlist=[]
wlist=[]
xlist=[]
ylist=[]
zlist=[]

dubslist=[]
tripslist=[]
quadslist=[]
quintslist=[]
sextslist=[]

stopflag=False

optionsu = {0 : 'face ',2 : 'arm',3 : 'l leg',4 : 'chest',5 : 'belly',6 : 'chest',7 : 'pubis',8 : 'ass',9 : 'feet',1 : 'hand '}
optionsw = {1 : 'left cheek',2 : 'right cheek',3 : 'draw hearts on all',4 : 'left ass cheek',5 : 'right ass cheek',6 : 'rear fuckhole',7 : 'left of clitty',8 : 'right of clitty',9 : 'above clitty',0 : 'tally marks'}
optionsv = {0 : 'owned by ___',2 : 'easy slut',3 : 'spitroast me',4 : 'free bj',5 : 'I swallow',6 : 'own me!',7 : 'use me!',8 : 'ready to serve',9 : 'slave',1 : 'fuck me'}
optionsx = {0 : 'ready to serve',2 : 'secondary hole',3 : 'cum in me',4 : 'fill me up',5 : 'needs cum',6 : 'rape me!',7 : 'cum dump',8 : 'fuck me',9 : 'I love sperm',1 : 'primary hole'}
optionsz = {0 : 'New tattoo',2 : 'take a butt pic and keep for a week',3 : 'take a ass pick and upload it',4 : 'take a short walk',5 : 'full frontal pic',6 : 'full frontal pic and keep',7 : 'full frontal pic and upload it',8 : 'pic on back spread, upload it',9 : 'take 5 pics or vids and upload',1 : 'take a ass pic'}

total=0
itr=-1

bg=False
vbg=False
if len(sys.argv) == 2:
    if sys.argv[1] == '-bg':  # Bad gambler mode
        bg=True
    if sys.argv[1] == '-vbg': # Very bad gambler mode
        vbg=True

while True:
    itr=itr+1
    ulist.append(randrange(10))
    vlist.append(randrange(10))
    wlist.append(randrange(10))
    xlist.append(randrange(10))
    ylist.append(randrange(10))
    zlist.append(randrange(10))

    if (bg or vbg):
        if zlist[itr] != ylist[itr]:
           zlist[itr]=randrange(10)
        if zlist[itr] != ylist[itr]:
           zlist[itr]=randrange(10)
        if xlist[itr] != ylist[itr]:
           xlist[itr] = randrange(10)
        if xlist[itr] != ylist[itr]:
           xlist[itr] = randrange(10)
        if wlist[itr] != xlist[itr]:
           wlist[itr] = randrange(10)
        if wlist[itr] != xlist[itr]:
           wlist[itr] = randrange(10)
        if vlist[itr] != wlist[itr]:
           vlist[itr] = randrange(10)
        if vlist[itr] != wlist[itr]:
           vlist[itr] = randrange(10)
        if ulist[itr] != vlist[itr]:
           ulist[itr] = randrange(10)
        if ulist[itr] != vlist[itr]:
           ulist[itr] = randrange(10)

    if vbg:
        if zlist[itr] != ylist[itr]:
           zlist[itr]=randrange(10)
        if zlist[itr] != ylist[itr]:
           zlist[itr]=randrange(10)
        if xlist[itr] != ylist[itr]:
           xlist[itr] = randrange(10)
        if xlist[itr] != ylist[itr]:
           xlist[itr] = randrange(10)
        if wlist[itr] != xlist[itr]:
           wlist[itr] = randrange(10)
        if wlist[itr] != xlist[itr]:
           wlist[itr] = randrange(10)
        if vlist[itr] != wlist[itr]:
           vlist[itr] = randrange(10)
        if vlist[itr] != wlist[itr]:
           vlist[itr] = randrange(10)
        if ulist[itr] != vlist[itr]:
           ulist[itr] = randrange(10)
        if ulist[itr] != vlist[itr]:
           ulist[itr] = randrange(10)


    if (list(set([1,2,3,4,5,6,7,8,9,0])^set(ulist)) and list(set([1,2,3,4,5,6,7,8,9,0])^set(xlist))):
        stopflag=False
    else:
       if ylist[itr] == 8:
          stopflag=True

    if ((ylist[itr] == 2) and (total > 20)):
        stopflag=True

    if ((ylist[itr] == 4) and (total > 40)):
        stopflag=True

    dubs=[ylist[itr],zlist[itr]]
    trips=[xlist[itr],ylist[itr],zlist[itr]]
    quads=[wlist[itr],xlist[itr],ylist[itr],zlist[itr]]
    quints=[vlist[itr],wlist[itr],xlist[itr],ylist[itr],zlist[itr]]
    sexts=[ulist[itr],vlist[itr],wlist[itr],xlist[itr],ylist[itr],zlist[itr]]

    cd=Counter(dubs)
    ct=Counter(trips)
    cq=Counter(quads)
    cqu=Counter(quints)
    cs=Counter(sexts)

    dubsl = [i for i, j in cd.items() if j > 1]
    if dubsl:
        dubslist.append(1)
    else:
        dubslist.append(0)

    tripsl = [i for i, j in ct.items() if j > 2]
    if tripsl:
        tripslist.append(1)
    else:
        tripslist.append(0)

    quadsl = [i for i, j in cq.items() if j > 3]
    if quadsl:
        quadslist.append(1)
    else:
        quadslist.append(0)

    quintsl = [i for i, j in cqu.items() if j > 4]
    if quintsl:
        quintslist.append(1)
    else:
        quintslist.append(0)

    sextsl = [i for i, j in cs.items() if j > 5]
    if sextsl:
        sextslist.append(1)
    else:
        sextslist.append(0)

    total=total+1
    if stopflag:
       break


print("{: ^15} {: ^25} {: ^40}".format('Where', 'What', 'Specials'))
for i in range(len(ylist)):
    special=''
    if ylist[i] == 0 and i > 5:
       special=optionsz[zlist[i]]

    if (sum([dubslist[i],tripslist[i],quadslist[i],quintslist[i],sextslist[i]]) > 0):
       special=special+' draw a cock'
       if sum([tripslist[i],quadslist[i],quintslist[i],sextslist[i]]) > 0:
           special=special+', draw tits'
           if sum([quadslist[i],quintslist[i],sextslist[i]]) > 0:
               special=special+', draw sperms'
               if sum([quintslist[i],sextslist[i]]) > 0:
                   special=special+', redraw maks each day for a week'
                   if sextslist[i] == 1:
                       special=special+' and get a tattoo!'


    if wlist[i] in [3,0]:
       special=special+' disregard "what" this round'

    print("{: ^15} {: ^25} {: ^40}".format(optionsu[ulist[i]], optionsv[vlist[i]], ''))
    print("{: ^15} {: ^25} {: ^40}".format(optionsw[wlist[i]], optionsx[xlist[i]], special))
