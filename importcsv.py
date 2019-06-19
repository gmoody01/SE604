import csv
import math

with open('DJIA.csv', 'r') as DJIA_file:
#    DJIA_reader = csv.reader(DJIA_file)
    DJIA_reader = csv.DictReader(DJIA_file)

    column = 
    sqrts = [math.sqrt(x) for x in column]
    print(sqrts)

 #   with open('DJIA_data.csv', 'w') as newDJIA_file:
  #      fieldnames = ['DATE', 'DJIA Value']

   #     for line in DJIA_reader:
    #        print(line)

