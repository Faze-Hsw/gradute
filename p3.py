import random
def p3():
    p3={}

    g1=round(random.random(),2)
    if g1>=0.5:
        p3[1]=g1
        p3[2]=1-g1
    else:
        p3[1]=1-g1
        p3[2]=g1

    g1=round(random.random(),2)
    if g1>=0.5:
        p3[5]=g1
        p3[7]=1-g1
    else:
        p3[5]=1-g1
        p3[7]=g1

    g1=round(random.random(),2)
    if g1>=0.5:
        p3[6]=g1
        p3[8]=1-g1
    else:
        p3[6]=1-g1
        p3[8]=g1
    return p3