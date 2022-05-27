import numpy as np 
x=np.array(["akash","rathore","elephantinforest","c++"],dtype=np.str)
print("original array")
print(x)
remove_space=np.char.strip(x)
print("\nremoving the leading and trailing white spaces:",remove_space)
