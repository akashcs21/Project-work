import numpy as np 
arr=np.array(["akash","rathore","course"],dtype="str")
print("original array:",arr)
multi_linesplit=np.char.splitlines(arr)
print(multi_linesplit)
