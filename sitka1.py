import csv
infile =open('sitka_weather_07-2018_simple.csv','r')
csvfile =csv .reader(infile,delimiter=',')  # breaks into a list
header_row = next(csvfile)

#print(header_row)
print(header_row)

for index,column_header in enumerate(header_row):
    print(index,column_header)

highs = []

for record in csvfile:
    highs.append(int(record[5]))

#check out highs
print(highs)

import matplotlib.pyplot as plt

#plot 
plt.plot(highs,c="red")
plt.title("Daily high temperature,July 2018",fontsize=16)
plt.xlabel("",fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",which ="major",labelsize=16)
plt.show()