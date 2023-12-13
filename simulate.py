from combination import target_list
from win_probablity import p
def produce():
    m=p()
    max_win=0
    best=()
    for x in target_list:
        c=1
        i=0
        for y in x:
            c*=m[i][y]
            i+=1
        if c>max_win:
            max_win=c
            best=x
    final_choice = []
    u = 1
    for x in m:
        max = 0
        c = 0
        for y in x.keys():
            if y in final_choice:
                continue
            if x[y] > max:
                c = y
                max = x[y]
        final_choice.append(c)
        u *= max
    return u/max_win
sum=0
for i in range(0,1000):
    sum+=produce()
print(sum/1000)