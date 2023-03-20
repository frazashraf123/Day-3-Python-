#Question.2
myList = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
l=[]
for i in list_b:    
    l.append((i,myList.index(i)))
print(l)

#list comprehension
print([(i,myList.index(i)) for i in list_b])

#dictionary
res={}
for i in list_b:    
    res[i]=myList.index(i)
print(res)

print({i:myList.index(i) for i in list_b}) 
