import numpy as np 
a=np.array([[1,2,3,3],[1,2,3,34]])
# sum=0
# for i in a:
#     sum+=i 
# print(sum)  
#sum of each elements by function 
# print(a.sum())
b=np.array([[1,2,3,4],[2,3,4,5]])
# print(np.add(a,b))
result=[[0,0,0,0],[0,0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result+=a[i][k]+b[k][j]
print(result) 
result=[[sum(a*b for a,b in zip(a_row,b_colom))for b_colom in zip(*b)] for a_row in a]
for i in result:
    print(i)         
