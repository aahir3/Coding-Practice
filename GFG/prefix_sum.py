def prefix_sum(arr):
    for i in range(1,len(arr)):
        arr[i]=arr[i]+arr[i-1]
    print(arr)

if __name__ == "__main__":
    a=list(map(int,input().split()))
    prefix_sum(a)