##import modules 
import csv
from datetime import datetime

#open files
infile =open('sitka_weather_07-2018_simple.csv','r')
csvfile =csv .reader(infile,delimiter=',') 
# skip the head
header_row = next(csvfile)

#print header_row
print(header_row)

for index,column_header in enumerate(header_row):
    print(index,column_header)

#create two emply lists 
highs =[]
dates = []

# load values into the lists 
for record in csvfile:
    highs.append(int(record[5]))
    thedate =datetime.strptime(record[2],'%Y-%m-%d')
    dates.append(thedate)

#check out data 
print(highs)
print(dates)

#import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()  

#plot 
plt.plot(dates,highs,c="red")
plt.title("Daily high temperature,July 2018",fontsize=16)
plt.xlabel("July 2018",fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",which ="major",labelsize=16)

# format date 
fig.autofmt_xdate()
plt.show()
