#Question 3.
sentences = ["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday","with over three lakh diya or earthen lamps","lit up simultaneously on the banks of sarayu river"]
stopwords = ['for','a','of','the','and','to','in','on','with','was']
l=[]
s=0
for i in sentences:
    z=i.split()
    for j in z:
        l.append(j)   
s=""
 
for i in l:
    if i not in stopwords:
        s+=i+" "
print(s)

result=[]
for sen in sentences:
    row_data=[]
    for words in sentences.split():
        if words not in stopwords:
            row_data.append(words)
    result.append(row_data)
print(result)

print([[word for word in sentence.split() if word not in stopwords]for sentence])
