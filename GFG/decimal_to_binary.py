def decimal_to_binary(n):
    binary_arr=[]
    if n == 0:
        return 0
    while(n > 0):
        binary_arr.append(str(n%2))
        n=n//2
    binary_arr.reverse()
    return int("".join(binary_arr)) 

if __name__ == "__main__":
    n=int(input())
    print(decimal_to_binary(n))