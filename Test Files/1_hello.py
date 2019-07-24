import re

str = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall("\S", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")