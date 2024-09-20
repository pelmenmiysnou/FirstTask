t=True
a=[float(i) for i in input().split()]
for i in a:
    b,c=str(i).split('.')
    if int(c) != 0:
        print("Ошибка, вводи целые!")
        t=False

if t==True:
    print(int(min(a)))

