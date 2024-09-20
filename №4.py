def triangle(x):
    n=int(x[0])
    s=x[2]
    for i in range((n+1)//2):
        print(s*(i+1))
    for i in range(n//2):
        print(s*(n//2-i))
a=input()
triangle(a)
    
    
