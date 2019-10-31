import sys, csv

#with open('Sales.csv', newline='') as csvfile:
fields = ['Transaction_date', 'Product', 'Price', 'Payment_Type', 'Name', 'City', 'State', 'Country', 'Account_Created', 'Last_Login', 'Latitude', 'Longitude']

reader = csv.DictReader(open('Sales.csv', newline=''),fieldnames=fields)
i=1
x=next(reader)
print("S.No.\t", x['City'], "\t\t\t\t|", x['Country'])
print("==============================================================")
for x in reader:
    print(i ,". \t", x['City'], "\t\t\t", x['Country'])
    i+=1

#   print(row)

#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#        print(', '.join(row))
