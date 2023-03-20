
#Question 4.
num="3,2,6,5,1,4,8,9"
l=list(map(int,num.split(",")))
iof5=l.index(5)
iof8=l.index(8)
num1=sum(l[:iof5])+sum(l[iof8+1:])
temp=list(map(str,l[iof5:iof8+1]))
num2="".join(temp)
op=int(num2)+num1
print(op)
