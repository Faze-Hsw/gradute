import random
def p1():
    p1={}

    g1=round(random.random(),2)
    if g1>=0.5:
        p1[1]=g1
        p1[5]=1-g1
    else:
        p1[1]=1-g1
        p1[5]=g1

    g1=round(random.random(),2)
    if g1>=0.5:
        p1[2]=g1
        p1[6]=1-g1
    else:
        p1[2]=1-g1
        p1[6]=g1

    g1=round(random.random(),2)
    if g1>=0.5:
        p1[3]=g1
        p1[7]=1-g1
    else:
        p1[3]=1-g1
        p1[7]=g1

    g1=round(random.random(),2)
    if g1>=0.5:
        p1[4]=g1
        p1[8]=1-g1
    else:
        p1[4]=1-g1
        p1[8]=g1
    return p1