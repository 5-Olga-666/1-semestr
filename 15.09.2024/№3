def palindrome(st):
    x = 1
    for i in range (len(st)//2):
        if st[i] != st[len(st)-1-i]:
            x = 0
            break
    return x
def mirrored (st):
    b = {'A':'A', 'B':0, 'C':0, 'D':0, 'E':'3', 'F':0, 'G':0, 'H':'H', 'I':'I', 'J':'L', 'K':0, 'L':'J', 'M':'M', 'N':0, 'O':'O', 'P':0, 'Q':0, 'R':0, 'S':'2', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'5', '0':'0', '1':'1', '2':'S', '3':'E', '4':0, '5':'Z', '6':0, '7':0, '8':'8', '9':0}
    y = 1
    for i in range (len(st)//2):
        if st[i] != b[st[len(st)-1-i]]:
            y = 0
            break
    if len(st)%2!=0:
        if st[len(st)//2]!='A' and st[len(st)//2]!='H' and st[len(st)//2]!='I' and st[len(st)//2]!='M' and st[len(st)//2]!='O' and st[len(st)//2]!='T' and st[len(st)//2]!='U' and st[len(st)//2]!='V' and st[len(st)//2]!='W' and st[len(st)//2]!='X' and st[len(st)//2]!='Y' and st[len(st)//2]!='0' and st[len(st)//2]!='1' and st[len(st)//2]!='8':
            y = 0
    return y    
a = input()
if palindrome(a)==1 and mirrored(a)==1:
    print(a+" is a mirrored palindrome.")
elif palindrome(a)==1 and mirrored(a)==0:
    print(a+" is a regular palindrome.")
elif palindrome(a)==0 and mirrored(a)==1:
    print(a+" is a mirrored string.")
else:
    print(a+" is not a palindrome.")
