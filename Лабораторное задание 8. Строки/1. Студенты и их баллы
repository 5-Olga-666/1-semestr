s=input()
a=[]
b=[]
for i in range(s.count('student_')-1):
    s=s[8::]
    a.append(s[:3:])
    s=s[3::]
    x=0
    while s[x]!='s':
        x=x+1
    b.append(int(s[:x:]))
    s=s[x::]
s=s[8::]
a.append(s[:3:])
s=s[3::]
b.append(int(s))
y=b[0]
z=0
for i in range (len(b)):
    if y<b[i]:
        z=i
print(a[z])

