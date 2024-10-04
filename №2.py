s=input()
q=''
q=q+s[1::-1]
x=s.find(' ')
q=q+s[2:x:]
q=q+"-"
s=s[x+1::]
q=q+s[1::-1]
q=q+s[2::]
print(q)
