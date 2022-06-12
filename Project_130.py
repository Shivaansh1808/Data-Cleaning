# Multiply each value in the radius column with 0.102763 to convert to solar radius.
# Multiply each value in the mass column with 0.000954588 to convert to solar mass.
# HOW TO DO THESE?
import csv
from unittest import skip
import pandas as pd

dataset_1 = []
dataset_2 = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

header1 = dataset_1[0]
header2 = dataset_2[0]

planetdata1 = dataset_1[1:]
planetdata2 = dataset_2[1:]

headers = header1+header2
planetdata = []

for index, data in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open("space_merged_stars_PRO-129.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

with open("space_merged_stars_PRO-129.csv", "r") as input, open("PRO-129_stars_merged.csv", "w",newline = "") as output:
    csvwriter = csv.writer(output)

    for row in csv.reader(input):
        if any(field.strip() for field in row):
            csvwriter.writerow(row)

temp_planet_data = list(planetdata)

for planet_data in temp_planet_data:

    planet_radius = planet_data[10]
    planet_mass = planet_data[9]

    if planet_mass == "unknown" or planet_mass == "" or planet_mass == " ":
        planetdata.remove(planet_data)
        continue
    else:
        planet_mass = float(planet_mass)*0.102763
        planet_data[9] = planet_mass
    
# For radius
    if planet_radius.lower() == "unknown" or planet_radius.lower() == "" or planet_radius.lower() == " ":
        planetdata.remove(planet_data)
        continue
    else:
        planet_radius = float(planet_radius) * 0.000954588
        planet_data[10] = planet_radius
    
#PROJECT 130

df = pd.read_csv("PRO-129_stars_merged.csv")
print(df.shape)

#del df["hyperlink"]
df.drop(["luminosity", "Unnamed: 0", "Unnamed: 6"], axis = 1, inplace= True) # inplace = in order (delete these one by one in order), axis=1 means reads row wise (horizontal)

#df = df.rename({}, axis = "columns")
print(df.columns)
print(df.shape)

df.to_csv("PRO-130_stars_merged.csv")