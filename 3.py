n=int(input())
def comb(s):
    for i,x in enumerate(s):
        for j in range(i,len(s)):
            yield [x,s[j]]
l=list(comb([0,1,2,5,6,8,9]))
p=[]
for i in l:
    a=''
    for j in i:
        a+=str(j)
    p.append(int(a))
    p.append(int(a[::-1]))
p=set(p)
p=list(p)
print(p[n])
