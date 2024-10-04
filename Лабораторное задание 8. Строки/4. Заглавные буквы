a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
c=dict(zip(a,b))
def bukva(x):
    y=0
    for i in range(len(a)):
        if x==a[i]:
            y=1
        else:
            y=0
    return y
s=input()
x=0
if len(s)>=4:
    for i in range(4):
        if s[i] in b:
            x=x+1
    if x>=3:
        s1=''
        for i in range(len(s)):
            if s[i] in a:
                s1=s1+c[s[i]]
            else:
                s1=s1+s[i]
        print(s1)
    else:
        print(s)
else:
    print(s)
                

