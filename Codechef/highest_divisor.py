n=int(input())
count_list=[1]
for i in range(2,11):
    if(n%i == 0):
        count_list.append(i)
print(max(count_list))