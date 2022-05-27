d={}
n=int(input("enter the size of dictionery: "))
for i in range(n):
    key=input("enter the key:")
    value=input("enter the value: ")
    d.update({key:value})
print(d)    
