import sys
import csv

txt=open("SalesJan2009.csv","r")
print(txt.readline())

for x in range(10):
    print(txt.readline())