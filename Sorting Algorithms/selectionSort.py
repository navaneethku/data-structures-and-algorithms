a = [2,5,7,3,4,8,1]
minI = 0
n = len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if(a[j]<a[minI]):
            minI = j
    if(minI!=i):
        a[i],a[minI] = a[minI],a[i]
print(a)
        