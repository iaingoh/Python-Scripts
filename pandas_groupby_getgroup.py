import csv
import pandas as pd

df = pd.read_csv("warranty_status.csv")
g = df.groupby('dental_outlet')
print(g)
print(g.get_group('LIVERPOOL DENTAL CARE'))
h = g.get_group('LIVERPOOL DENTAL CARE')
print(h.count())
start_count = h.count().warranty_start
total_count = h.count().dental_outlet
non_count = total_count - start_count

print(start_count)
print(total_count)
print(non_count)


















