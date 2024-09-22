N=int(input())
M=int(input())
a=[]
for i in range(N):
    a.append([0]*M)
v=0
n=N-1
l=0
p=M-1
k=1
while v<=n and l<=p:
    for i in range(l,p+1):
        a[v][i]=k 
        k=k+1
    v=v+1
    for i in range(v,n+1):
        a[i][p]=k
        k=k+1
    p=p-1
    if v<=n:
        for i in range(p,l-1,-1):
            a[n][i]=k
            k=k+1
        n=n-1
    if l<=p:
        for i in range(n,v-1,-1):
            a[i][l]=k
            k=k+1
        l=l+1
for i in range(N):
    for j in range(M):
        a[i][j]=str(a[i][j])
    print(' '.join(a[i]))
for i in range(N):
    for j in range(M):
        a[i][j]=str(a[i][j])
    print(' '.join(a[i])*i)
