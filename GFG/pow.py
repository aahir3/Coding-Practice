def pow(a,n):
    if(n == 0):
        return 1
    if(n == 1):
        return a
    elif(n%2 == 0):
        temp=pow(a,n//2)
        return temp*temp
    else:
        t=pow(a,(n-1)//2)
        return t*t*a

if __name__ == "__main__":
    x=int(input())
    y=int(input())
    ans=pow(x,y)
    print(ans)