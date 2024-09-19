q = input()
n = int(q[0])
a = q[1::]
s = ''
l = len(a)-1
g = l//n
for i in range (g):
    s = s + a[((i+1)*n):(i*n):-1]
print(s)
    
