import csv
from datetime import datetime
from matplotlib import pyplot as plt

# open both the files in read mode
infile1 =open('death_valley_2018_simple.csv','r')
infile2 =open('sitka_weather_2018_simple.csv','r')

#read and split the content of each files to list
csvfile1 =csv.reader(infile1,delimiter=',')  #
csvfile2 =csv.reader(infile2,delimiter=',')  

#seperate the header row of csv file
header_row_death_valley = next(csvfile1)
header_row_sitka = next(csvfile2)

# print(header_row_death_valley)
print(header_row_death_valley)
# print(header_row_sitka)
print(header_row_sitka)

#for using automatic indexes , 
name_index_pos1 = header_row_death_valley.index('NAME')
thedate_index_pos1 = header_row_death_valley.index('DATE')
high_index_pos1 = header_row_death_valley.index('TMAX')
low_index_pos1 = header_row_death_valley.index('TMIN')

name_index_pos2 = header_row_sitka.index('NAME')
thedate_index_pos2 = header_row_sitka.index('DATE')
high_index_pos2 = header_row_sitka.index('TMAX')
low_index_pos2 = header_row_sitka.index('TMIN')

#create empty list to store the corresponding extracted data
dates1,highs1,lows1,name1 =[],[],[],[]
dates2,highs2,lows2,name2 =[],[],[],[]

#loop to pull all min and max temps along with the dates of death valley 
for record in csvfile1:
    name1 = record[name_index_pos1]
    #print(name1)
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

#loop to pull all min and max temps along with the dates of Sitka
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
# print(lows)
# print(dates)
fig = plt.figure()  

#using suplot to draw multiple plots in smae window 
#
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

#to plot the graphs
plt.show()
#for dates to format it into readable format or else its will be collapsed
fig.autofmt_xdate()



