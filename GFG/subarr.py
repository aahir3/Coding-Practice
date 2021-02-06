def rotate_arr(arr,k):
    while(k > len(arr)):
        k=k%len(arr)
    return arr[-k:]+arr[:-k]

if __name__ == "__main__":
    n,k,q=list(map(int,input().split()))
    queries=[]
    arr=list(map(int,input().split()))
    for _ in range(q):
        queries.append(int(input()))
    b=rotate_arr(arr,k)
    for _ in range(q):
        print(b[queries[_]])