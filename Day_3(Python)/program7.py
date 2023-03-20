

#Question 5.

d={"rhdt":"246","ghftd":"1246"}
suml=[]
for i in d.values():
    sum=0
    for j in i:
        sum=sum+(int(j)*int(j))     
    suml.append(sum)
print(suml)
j=0
for i in d.keys():
    if(int(suml[j])%2!=0):
        print(i[1:]+i[0])
    else:
        print(i[2:]+i[0]+i[1])
    j+=1    

'''
#OR
s=input().split(",") #rhdt:246, ghftd: 1246
stt=[]
numm= []
for i in s:
    s1,n=i.split(":")
    stt.append(s1) #stt= [rhdt, ghftd]
    numm.append(n) #numm= [246, 1246]
def rotate(ss,n) : #ss=rhdt, n=246
    n=str(n)
    s=0
    for i in n:#
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1] # rhdt
    else:
        return ss[2:]+ss[:2]

for i in range (len(numm)) : #i=0
    print(rotate(stt[i],numm[i]))
