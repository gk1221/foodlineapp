import pandas as pd

value = ['1','2','3']
value1 = ['4','5']

v = [value, value1]

df = pd.DataFrame(v)
df.to_csv('d.csv', header=False)

