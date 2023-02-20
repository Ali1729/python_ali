import csv 
import os

file_name = "DimenLookupAge8277.csv"

# with open("C:\Users\LENOVO\Documents\python_ali\Projects\csv_pandas\\"+str(file_name)) as fp:

with open(r"C:\Users\LENOVO\Documents\python_ali\Projects\csv_pandas\\"+str(file_name)) as fp:
# with open(os.getcwd()+os.sep+file_name) as fp:
    a = csv.DictReader(fp)


    for row in a:
        print(row)

a = csv.DictReader(open('my_file.csv'))