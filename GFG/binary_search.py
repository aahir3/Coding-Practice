def binary_search(arr,l,r,k):
    while(l <= r):
        mid=l+(r-l)//2
        if(arr[mid] == k):
            return mid
        elif(arr[mid] < k):
            l=mid+1
        else:
            r=mid-1
    return -1
  





if __name__ == "__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    ans=binary_search(arr,0,n-1,k)
    if(ans != -1):
        print("Found at :",ans)
    else:
        print("Not Found")