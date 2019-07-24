import sys
import csv

with open('Sales.csv', newline='') as csvfile:
    fields = ['Transaction_date', 'Product', 'Price', 'Payment_Type', 'Name', 'City', 'State', 'Country', 'Account_Created', 'Last_Login', 'Latitude', 'Longitude']

    reader = csv.DictReader(csvfile,fieldnames=fields)
    for row in reader:
        print(row['City'], row['Country'])
#        print(row)

#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')    
#    for row in spamreader:
#        print(', '.join(row))
        

    