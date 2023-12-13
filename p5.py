import random
def p5():
    p5 = {}

    g1=round(random.random(),2)
    if g1 >= 0.5:
        p5[1] = g1
        p5[8] = 1 - g1
    else:
        p5[1] = 1 - g1
        p5[8] = g1

    g1=round(random.random(),2)
    if g1 >= 0.5:
        p5[2] = g1
        p5[7] = 1 - g1
    else:
        p5[2] = 1 - g1
        p5[7] = g1

    g1=round(random.random(),2)
    if g1 >= 0.5:
        p5[3] = g1
        p5[6] = 1 - g1
    else:
        p5[3] = 1 - g1
        p5[6] = g1

    g1=round(random.random(),2)
    if g1 >= 0.5:
        p5[4] = g1
        p5[5] = 1 - g1
    else:
        p5[4] = 1 - g1
        p5[5] = g1
    return p5