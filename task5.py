#import math
#def f(x):
#    if x[0] ==0 and x[1]==0: return None
#    if x[0]==0 and x[1]>0 :return 1.5707963267948966
#    if x[0]==0 : return 4.710796326794897
#    if x[0]<0 and x[1]<0: return math.atan(x[1]/x[0])+3.14
#    if x[0]<0: return math.atan(x[1]/x[0])+3.14
#    return math.atan(x[1]/x[0])+6.28
#a=[float(i) for i in input('x y').split()]
#b=[float(i) for i in input('x y').split()]
#c=[float(i) for i in input('x y').split()]
#if f(a)<f(b) and f(a)<f(c):print(a)
#elif f(b)<f(c): print(b)
#else: print(c)

def es(x):
    b=True
    if x<2:return(False)
    for i in range(1,x):
        if x%i==0 and i>1 :
            b=False
            break
    return(b)


def pol(x):
    b=bin(x)[2:]
    f=True
    for i in range(len(b)):
        if b[i]!=b[-(i+1)]:
            f=False
            break
    return(f)
a=[]
n=int(input())
for i in range(2,n):
    if es(i) and pol(i):
        a.append(i)
print(a)
