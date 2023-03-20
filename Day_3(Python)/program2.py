#for loop version
result=[]
for i in range(11):
    result.append(i)
print(result)

#list comprehension
print([i for i in range(11)])
re=[]
for i in range(11):
    if(i%2!=0):
        re.append(i)
print(re)
print([i for i in range(11) if i%2!=0]) 
