#list comprehension
print([i if i%2!=0 else i**2 for i in range(11)]) 
 
#matrix
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if(ele%2!=0):
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result)    
            
print([[ele**2 if ele%2!=0 else ele**3 for ele in row] for row in mat])
