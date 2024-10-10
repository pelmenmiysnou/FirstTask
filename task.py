a= int(input())
s=0
for i in range(1,a+1):
    s+=i**3
print(s)


for i in range(1,10):
    for j in range(1,10):
        print("%3d" % (i * j), end="")
    print()
    
        
for i in range(9,0,-1):
    for j in range(1,10):
        print("%3d" % (i * j), end="")
    print()
