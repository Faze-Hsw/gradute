import random
def p2():
    p2={}

    g1=round(random.random(),2)
    if g1>=0.5:
        p2[3]=g1
        p2[4]=1-g1
    else:
        p2[3]=1-g1
        p2[4]=g1

    g1=round(random.random(),2)
    if g1>=0.5:
        p2[5]=g1
        p2[6]=1-g1
    else:
        p2[5]=1-g1
        p2[6]=g1

    g1=round(random.random(),2)
    if g1>=0.5:
        p2[7]=g1
        p2[8]=1-g1
    else:
        p2[7]=1-g1
        p2[8]=g1
    return p2