import numpy as np
arr=[]
size=int(input("how many numbers you want to insert"))
for i in range(size):
    value=int(input("enter value "))
    arr.append(value)
my_array=np.array(arr)