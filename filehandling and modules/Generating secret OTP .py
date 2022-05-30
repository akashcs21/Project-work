import random as rd
import secrets as sc 
otp=sc.SystemRandom() 
print("your random secure otp:")
print(otp.randrange(123569,999999))
#by using random module 
print("secret OTP is:")
print(rd.randrange(100000,999999))
