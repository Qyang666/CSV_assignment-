#import modules 
import csv
from datetime import datetime

#open csv data  
infile =open('sitka_weather_2018_simple.csv','r')
csvfile =csv .reader(infile,delimiter=',')  

#skip the first row 
header_row = next(csvfile)

#print(header_row)
print(header_row)

for index,column_header in enumerate(header_row):
    print(index,column_header)

#create empty lists 
highs =[]
dates = []
lows = []

#load data into lists 
for record in csvfile:
    highs.append(int(record[5]))
    lows.append(int(record[6]))
    thedate =datetime.strptime(record[2],'%Y-%m-%d')
    dates.append(thedate)

#check out data 
print(highs)
print(lows)
print(dates)

#import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()  

#plot 
plt.plot(dates,highs,c="red")
plt.plot(dates,lows,c="blue")

#set alphat to 0.1
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title("Daily High temperature- 2018",fontsize=16)
plt.xlabel("July 2018",fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",which ="major",labelsize=16)

# format date 
fig.autofmt_xdate()

#plot 
plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")
plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")
plt.suptitle("Highs and lows of Sitka,Alaska")
plt.show()