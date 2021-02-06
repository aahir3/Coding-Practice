import math
def fun():
    a=math.sqrt((x[1]-x[0])**2+(y[1]-y[0])**2)
    b=math.sqrt((x[2]-x[1])**2+(y[2]-y[1])**2)
    c=math.sqrt((x[2]-x[0])**2+(y[2]-y[0])**2)
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('%.8f'%area)
x=[]
y=[]
for _ in range(3):
    a,b=list(map(float,input().split()))
    x.append(a)
    y.append(b)
fun()