import csv 
import os

file_name = "DimenLookupAge8277.csv"

with open(file_name) as fp:
    a = csv.DictReader(fp)


print(a)