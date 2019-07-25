import sys
import csv

#with open('Sales.csv', newline='') as csvfile:
fields = ['Transaction_date', 'Product', 'Price', 'Payment_Type', 'Name', 'City', 'State', 'Country', 'Account_Created', 'Last_Login', 'Latitude', 'Longitude']

reader = csv.DictReader(open('Sales.csv', newline=''),fieldnames=fields)
x=next(reader)
print(x['City'], x['Country'])
x=next(reader)
print(x['City'], x['Country'])
x=next(reader)
print(x['City'], x['Country'])
x=next(reader)
print(x['City'], x['Country'])
x=next(reader)
print(x['City'], x['Country'])
x=next(reader)
print(x['City'], x['Country'])
x=next(reader)
print(x['City'], x['Country'])
x=next(reader)
print(x['City'], x['Country'])
#   print(row)

#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')    
#    for row in spamreader:
#        print(', '.join(row))
        

    