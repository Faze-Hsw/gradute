import random
def p4():
    p4={}

    g1=round(random.random(),2)
    if g1>=0.5:
        p4[1]=g1
        p4[3]=1-g1
    else:
        p4[1]=1-g1
        p4[3]=g1

    g1=round(random.random(),2)
    if g1>=0.5:
        p4[2]=g1
        p4[4]=1-g1
    else:
        p4[2]=1-g1
        p4[4]=g1
    return p4