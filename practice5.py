#import modules
import csv
from datetime import datetime
from matplotlib import pyplot as plt

# read files
file_death_valley =open('death_valley_2018_simple.csv','r')
file_sitka_weather =open('sitka_weather_2018_simple.csv','r')
csvfile1 =csv.reader(file_death_valley,delimiter=',')  #
csvfile2 =csv.reader(file_sitka_weather,delimiter=',')  

#skil the head row 
header_row_death_valley = next(csvfile1)
header_row_sitka = next(csvfile2)

# checkout 
print(header_row_death_valley)
# checkout 
print(header_row_sitka)


name_index_pos1 = header_row_death_valley.index('NAME')
thedate_index_pos1 = header_row_death_valley.index('DATE')
high_index_pos1 = header_row_death_valley.index('TMAX')
low_index_pos1 = header_row_death_valley.index('TMIN')

name_index_pos2 = header_row_sitka.index('NAME')
thedate_index_pos2 = header_row_sitka.index('DATE')
high_index_pos2 = header_row_sitka.index('TMAX')
low_index_pos2 = header_row_sitka.index('TMIN')

#create empty lists
dates1,highs1,lows1,name1 =[],[],[],[]
dates2,highs2,lows2,name2 =[],[],[],[]

#load data into lists 
for record in csvfile1:
    name1 = record[name_index_pos1]
    try:
         thedate =datetime.strptime(record[thedate_index_pos1],'%Y-%m-%d')
         high =int(record[high_index_pos1])
         low = int(record[low_index_pos1])

    except ValueError:
        print(f"Missing data for {thedate}")

    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(thedate)

#load sitka data 
for record in csvfile2:
    name2 = record[name_index_pos2]
    #print(name2)
    try:
         thedate =datetime.strptime(record[thedate_index_pos2],'%Y-%m-%d')
         high =int(record[high_index_pos2])
         low = int(record[low_index_pos2])

    except ValueError:
        print(f"Missing data for {thedate}")

    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(thedate)

# print(highs)
print(highs2)
# print(lows)
print(lows2)
# print(dates)
print(dates2)
fig = plt.figure()  

#plot 
plt.subplot(2,1,1)
plt.plot(dates1,highs1,c="red")
plt.plot(dates1,lows1,c="blue")

title1 = name1
plt.title(title1, fontsize = 16)
plt.fill_between(dates1,highs1,lows1, facecolor="blue", alpha=0.1)
plt.subplot(2,1,2)
plt.plot(dates2,highs2,c="red")
plt.plot(dates2,lows2,c="blue")

title2 = name2
plt.title(title2, fontsize = 16)
plt.fill_between(dates2,highs2,lows2, facecolor="blue", alpha=0.1)
plt.xlabel(" ",fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",which ="major",labelsize=16)
plt.suptitle (f"Temperature comparison between {name1} and {name2}")
plt.show()

#format date 
fig.autofmt_xdate()



