import csv 
import os

file_name = "DimenLookupAge8277.csv"

# with open(os.getcwd()+os.pathsep+file_name) as fp:
#     a = csv.DictReader(fp)


#     for row in a:
#         print(row)

a = csv.DictReader(os.getcwd()+os.pathsep+open(file_name))
print(a)