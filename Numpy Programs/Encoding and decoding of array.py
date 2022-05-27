# encodig and decoding of array
import numpy as np 
x=np.array(["akash","rathore","elephantinforest","c++"],dtype=np.str)
encoded_char=np.char.encode(x,"cp500")
decoded_char=np.char.decode(encoded_char,"cp500")
print("encoded_char=",encoded_char)
print("decoded_char=",decoded_char)
