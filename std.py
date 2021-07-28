import csv
import pandas as pd
import plotly.express as px
import math
f=open("data1.csv")
reader=csv.reader(f)
data=list(reader)

add=0
d=[]
for i in (data[0]):
    add=add+int(i)
    d.append(int(i))

mean=add/len(d)
l=0
print(mean)
for i in data[0]:
    a=int(i)-mean
    sq=a*a
    l=l+sq
std=math.sqrt(l/(len(d)-1))
print (std)

