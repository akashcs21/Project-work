def reverse(str):
    new_str=" "
    x=len(str)
    for i in range(x-1,-1,-1):
        new_str+=str[i]
    return new_str    
str=input("enter the string: ")
result=reverse(str)
print(result)      
        
