import numpy as np 
deg=float(input("enter the angle:"))
rd=np.deg2rad(deg)
radius=float(input("enter the radius:"))
print("Arc length of of angle is:")
arc_lenth=rd*radius
print(arc_lenth)
