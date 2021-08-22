import pandas as pd 

table = pd.read_csv("013_data.txt", header = None, usecols = [0]) 
sum = 0 
for x in range(len(table)):
    sum += int(table[0][x])

print(str(sum)[:10])

