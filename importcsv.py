import csv
import math

with open('DJIA.csv', 'r') as cvs_file:
   cvs_reader = csv.reader(cvs_file)

   for line in cvs_reader:
        print(line)


#    column =
#    sqrts = [math.sqrt(x) for x in column]
#    print(sqrts)

#with open('DJIA_data.csv', 'w') as newDJIA_file:
#      fieldnames = ['DATE', 'DJIA Value']
