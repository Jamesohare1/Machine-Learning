#Import Numpy
import numpy as np
import pandas as pd

# QUESTION 1 --------------------------------------------------------------------------------------------------

#0 Year
#1 Month (1 = Jan, 2 = Feb, 3 = March, etc. )
#2 Total Rainfall (Millimetres)
#3 Most Rainfall in a Day (Millimetres)
#4 Number of Rain days (A day is classified as a rain day if it has >= 0.2mm rain) (Number)

#Import Cork data set
corkData = np.array(np.loadtxt(fname = "./dataSets/CorkRainfall.txt"))

#(i)
print("most rainfall in a day: ", np.max(corkData[:,3]))  # max rainfall in a day
print("average rainfall in a day: ", np.mean(corkData[:,3])) # average rainfall in a day

#--------------------------------------------------------------------------------------------------

#(ii)
print(np.unique(corkData[:,0])) #display all unique years

year = input("Please select a year: ") #Promt user to enter year
year = int(year) #Convert input to an integer
numDays =  np.sum(corkData[:,4][corkData[:,0] == year]) #sum all rain days for that year
print("Numbers of days rain in ", year, ": ",  numDays) #, corkData[:,4]))

#--------------------------------------------------------------------------------------------------

#(iii)
months = {
     1: "January",
     2: "February",
     3: "March",
     4: "April",
     5: "May",
     6: "June",
     7: "July",
     8: "August",
     9: "September",
     10: "October",
     11: "November",
     12: "December"
        }
totalMthlyRain = np.empty(13)
for i in range(13):
    totalMthlyRain[i] = np.sum(corkData[:,2][corkData[:,1] == i])
maxRain = np.max(totalMthlyRain)
result = np.where(totalMthlyRain == maxRain)[0][0]
print("The wettest month is ",  months[result])



#(iv)
totalRows = np.size(corkData[:,1])
threshold = input("Please enter a threshold: ")
threshold = int(threshold)
numDaysBelow = np.size(corkData[:,4][corkData[:,4] <= threshold])
print("Percentage of rain days below threshold: ", numDaysBelow/totalRows)

#(v)
summerRain = np.mean(corkData[(corkData[:,1]>=6) & (corkData[:,1]<=8)][:,2])
autumnRain = np.mean(corkData[(corkData[:,1]>=9) & (corkData[:,1]<=11)][:,2])
print("Average Summer Rain is ", summerRain)
print("Average Summer Rain is ", autumnRain)

#(vi)
#Import Cork data set
dublinData = np.array(np.loadtxt(fname = "./dataSets/DublinRainfall.txt"))
allData = np.concatenate((corkData, dublinData))
print("average number of raindays: ", np.mean(allData[:,4]))

# QUESTION 2 --------------------------------------------------------------------------------------------------


#0. instant: record index
#1. season : season (1:springer, 2:summer, 3:fall, 4:winter)
#2. yr : year (0: 2011, 1:2012)
#3. mnth : month ( 1 to 12)
#4. hr : hour (0 to 23)
#5. holiday : weather day is holiday or not (extracted from [Web Link])
#6. weekday : day of the week
#7. workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
#8. + weathersit :
#i. 1: Clear, Few clouds, Partly cloudy, Partly cloudy
#ii. 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
#iii. 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain
#+ Scattered clouds
#iv. 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
#9. temp : Normalized temperature in Celsius. The values are divided to 41 (max)
#10. atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
#11. hum: Normalized humidity. The values are divided to 100 (max)
#12. windspeed: Normalized wind speed. The values are divided to 67 (max)
#13. casual: count of casual users
#14. registered: count of registered users
#15. cnt: count of total rental bikes including both casual and registered


#Import data set
import csv
file = open("./dataSets/bike.csv")
read = csv.reader(file)
bikeData = np.array(list(read))
bikeData = bikeData.astype(float)


#(i)
print(np.mean(bikeData[:,9]*41))


#(ii)
print(np.mean(bikeData[:,13][bikeData[:,5] == 1])) # average casual users on a  holiday
print(np.mean(bikeData[:,13][bikeData[:,5] == 0])) # average casual users on a non-holiday


#(iii)
months = {
     1: "Jan",
     2: "Feb",
     3: "Mar",
     4: "Apr",
     5: "May",
     6: "Jun",
     7: "Jul",
     8: "Aug",
     9: "Sep",
     10: "Oct",
     11: "Nov",
     12: "Dec"
        }
totalCasUsers = np.empty(13)
for i in range(1, 13):
    casUsers = np.sum(bikeData[:,13][bikeData[:,3] == i])
    print("number of casual users in ",  months[i], ": ", casUsers)


#(iv)
ranges = {
    1: (1,6),
    2: (6,10),
    3: (10,15),
    4: (15,20),
    5: (20,25),
    6: (25,30),
    7: (30,35),
    8: (35,40)}   

for i in range(1,9):
    casUsers = np.mean(bikeData[:,15][(bikeData[:,9]*41 >= ranges[i][0]) 
                                    &( bikeData[:,9]*41 < ranges[i][1])])
    print("number of casual users in range",  ranges[i], ": ", casUsers)

 




# QUESTION 3 --------------------------------------------------------------------------------------------------
#0. Case Number
#1. Date
#2. Year
#3. Type
#4. Country
#5. Area
#6. Location
#7. Activity
#8. Name
#9. Sex
#10. Age
#11. Injury
#12. Fatal
#13. Time
#14. Species
#15. Investigator or Source
    
#import statistics as st
df = pd.read_csv('./dataSets/attacks.csv', encoding = "ISO-8859-1")

df[df["Fatal"] == "n"] = "N"
df[df["Fatal"] == "UNKNOWN"] = "N"
df[df["Fatal"] == " N"] = "N"
df[df["Fatal"] == " N "] = "N"
df[df["Fatal"] == "2017"] = "N"
df[df["Fatal"] == "F"] = "N"
df[df["Fatal"] == "#VALUE!"] = "N"

#(i)
print(df.loc[:,"Location"].mode())


#(ii)
print(df.loc[:,"Country"].value_counts()[:6])


#(iii)
print(df.loc[:,"Country"][df.loc[:,"Fatal"] == "Y"].value_counts()[:6])


#(iv)
print(df.loc[:,"Activity"][df.loc[:,"Activity"]  == "Surfing"].value_counts())
print(df.loc[:,"Activity"][df.loc[:,"Activity"]  == "Scuba Diving"].value_counts())

#(v)
totalAttacks = np.size(df.loc[:,"Fatal"])
totalFatal = df.loc[:,"Fatal"][df.loc[:,"Fatal"] == "Y"].value_counts()
print("percentage of attacks which are fatal: ", totalFatal[0]/totalAttacks * 100)


#(vi)
Attacks_F  = df[["Country", "Fatal"]].where(df["Fatal"] == "Y").groupby(["Country"]).count()
Attacks_NF = df[["Country", "Fatal"]].where(df["Fatal"] == "N").groupby(["Country"]).count()
Attacks = pd.merge(Attacks_F, Attacks_NF, on = "Country", how = "inner")
Fatalpercent = Attacks["Fatal_x"] / (Attacks["Fatal_x"] + Attacks["Fatal_y"]) * 100
print(Fatalpercent)

