a = [2,5,7,3,4,8,1]
i = 0
j = 0
for i in range(len(a)):
    j = i
    while(j>0 and a[j-1]>a[j]):
        a[j],a[j-1] = a[j-1],a[j]
        j-=1
print(a)