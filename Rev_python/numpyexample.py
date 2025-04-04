import numpy as np 
ar = np.array([[1,2],[3,4]])
print(ar)  
ar2 = np.arange(0,10,2)
ar3 = np.linspace(0,1,100)
print(ar[-1])
print(ar2)

# Pandas
import pandas as pd
d = [10,20,30,40,50]
# s = pd.Series(d, indesx = ['a', 'b','c','d','e'])
# print(s)  # prints the series

di = {
    "name" : ["Arul", "Priya"],
    "city" : ["chennai", "hyd"]

}
df = pd.DataFrame(di)
print(df)  # prints the dataframe