import pandas as  pd

a = pd.DataFrame([[23,23],[12,12]])
print(a)

b = pd.DataFrame([[1,2],[3,4]])
print(b)

a = a.append(b)
print(a)