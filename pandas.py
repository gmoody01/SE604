import csv

# open the file in universal line ending mode 
with open('data.csv', 'r') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

# extract the variables from data.csv
date = data['date']
time = data['time']
temp = data['temperature_c']
#print(date)
#print(time)
#print(temp)

# convert list to string (practice - unnecessary for this program)
#str_date = ''.join(date)
#print(str_date)
#date_float = float(str_date)
#print(date_float)

#convert date from a list of numbers beginning with 1 to calendar date based on user input
#start_date = input("Enter the start date for this data set in MM/DD/YY format: ")
#need to create code that will return an error if invalid data entered
#for i in range(0, len(date)):
#need to create code that will read current 'date' info and replace/increment based on user input start date    

# convert time list to integers (practice - unnecessary for this program)
#for i in range(0, len(time)):
#    time[i] = int(time[i])

#print(time)

# convert time from 24hr to 12hr
for i in range(0, len(temp)):
    hours, minutes = time[i].split(":")
    hours, minutes = int(hours), int(minutes)
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours -= 12
    time[i] = (("%02d:%02d" + setting) % (hours, minutes))

#print(time)

# convert temperature list to decimal numbers
for i in range(0, len(temp)): 
    temp[i] = float(temp[i])
    
#print(temp)

# convert temp celsius to temp fahrenheit
for i in range(0, len(temp)):
    temp[i] = (temp[i] * 1.8) + 32

#print(temp)

#convert temp fahrenheit from decimal numbers to string
for i in range(0, len(temp)):
    temp[i] = str(temp[i])
    
#print(temp)

#write data to new data2.csv file to include 12hr time instead of 24hr time and fahrenheit temperature instead of celsius
        
rows = zip(date,time,temp)
with open('data2.csv', 'w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)