def cube(number):
    return number**3
number=int(input("enter the number: "))
x=cube(number)
print(f"the cube of number is:{x}") 
def by_three(number):
    if number%3==0:
        result=cube(number)
        return result
    else:
        return False
number=int(input("enter the number: "))        
x=by_three(number)
print(x)    
