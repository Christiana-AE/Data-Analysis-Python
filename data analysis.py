import csv
import json
import numpy as np
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import re
import statistics
import seaborn as sns



# Opening the file named 'Inspections' 
df_inspections = pd.read_csv("Inspections.csv")

# Openining the file named 'Inventory' 
df_inventory = pd.read_csv("Inventroy.csv")

# Opening the file named 'Violations'
df_violations = pd.read_csv("violations.csv")


#----------------------------- Cleaning Data ---------------------------------------------------------------------------------------------------

# Trimming the data in 'Activity Date' and converting from string to date time

df_inspections["ACTIVITY DATE"] = df_inspections["ACTIVITY DATE"].str.strip()
dateparse = lambda x: pd.datetime.strptime(x, "%m/%d/%Y")
df_inspections = pd.read_csv("Inspections.csv", parse_dates = ["ACTIVITY DATE"], date_parser = dateparse)


# Replace missing value in 'Zip codes' with 0
df_inspections = df_inspections.fillna(0)


# Remove data from column 'Score' where value is missing 
df_inspections = df_inspections[df_inspections["SCORE"] != 0] 


# Remove data from vendors with program status of 'Inactive'
df_inspections = df_inspections[df_inspections["PROGRAM STATUS"] != "INACTIVE"]


# Extract number of seating to a new column 
my_regex=re.compile(".*?\((.*?)\)")
df_inspections["PE_TYPE"] = df_inspections["PE DESCRIPTION"].str.extract(my_regex, expand = True)
df_inspections["PE DESCRIPTION"] = df_inspections["PE DESCRIPTION"].str.replace(r"\([^()]*\)", "", regex=True)


#----------------------------- Requirement 3  ---------------------------------------------------------------------------------------------------

# Calculate mean inspection score per year (per vendor seating)
df_inspections["YEAR"] = pd.to_datetime(df_inspections["ACTIVITY DATE"]).dt.to_period("Y") # create separate column for year from Activity Date

mean_vendor = df_inspections.groupby(["YEAR", "PE DESCRIPTION"])["SCORE"].mean()


# Calculate median inspection score per year (per vendor seating)
median_vendor = df_inspections.groupby(["YEAR", "PE DESCRIPTION"])["SCORE"].median()


# Calculate mode inspection score per year (per vendor seating)

vendor_count = df_inspections.groupby(["YEAR", "PE DESCRIPTION"])["SCORE"].value_counts() # calculates the count of score grouped by year & PE Description
mode_vendor = df_inspections.groupby(["YEAR", "PE DESCRIPTION"])["SCORE"].apply(lambda x:x.mode()) # calculates the mode


# Calculate mean inspection score per year (per zip code)
mean_zipcode = df_inspections.groupby(["YEAR", "Zip Codes"])["SCORE"].mean()


# Calculate median inspection score per year (per zip code)
median_zipcode = df_inspections.groupby(["YEAR", "Zip Codes"])["SCORE"].median()


# Calculate mode inspection score per year (per zip code)
zipcode_count = df_inspections.groupby(["YEAR", "Zip Codes"])["SCORE"].value_counts() # calculates the count of score grouped by year & Zip code
mode_zipcode = df_inspections.groupby(["YEAR", "Zip Codes"])["SCORE"].apply(lambda x:x.mode()) # calculates the mode


#----------------------------- Requirement 4  ----------------------------------------------------------------------------------------------------

# Grouping data of violations committed per establishment
grouped_data = df_violations.groupby(["VIOLATION CODE"])["SERIAL NUMBER"].nunique() 
#print(grouped_data.plot(kind = "bar"))


#----------------------------- Requirement 5  ----------------------------------------------------------------------------------------------------

# Create a new column 'Counts' to contain resulting Serial Number / Violation Code groupby values 

df_violations["Counts"] = df_violations.groupby(["SERIAL NUMBER"])["VIOLATION CODE"].transform("count")

# Merge df_violations and df_inspections using matching column - 'SERIAL NUMBER'
df_violations = pd.merge(df_violations, df_inspections, on = "SERIAL NUMBER", how = "inner")


# Calculate the correlation using Spearman correlation 
x = df_violations["Zip Codes"]
y = df_violations["Counts"]
df = pd.DataFrame({"x" : x, "y" : y})
corr = df.corr(method = "spearman")
print (corr)

# plot visualization for correlation 
heatmap = sns.heatmap(corr, annot = True)
plt.show()

#----------------------------- Translation to JSON  ----------------------------------------------------------------------------------------------------

inspections = df_inspections.to_csv("Inspections_.csv")
inventory = df_inventory.to_csv("Inventory_.csv")
violations = df_violations.to_csv("Violations_.csv")


# Transalate files to JSON format - Inspections file 

def inspections_json(csvInspections, jsonInspections):
    data = {}
    
    with open (csvInspections) as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows ["ACTIVITY DATE"]
            data[key] = rows
    with open (jsonInspections, "w") as jsonf:
        jsonf.write(json.dumps(data, indent = 4))

# Create Inspection JSON paths 
csvInspections = r"Inspections_.csv"
jsonInspections = "Inspections.json"
inspections_json(csvInspections, jsonInspections)


# Translate files to JSON format - Inventory file 

def inventory_json (csvInventory, jsonInventory):
    data2 = {}
    with open (csvInventory) as csvf2:
        csvReader = csv.DictReader(csvf2)
        for rows in csvReader:
            key2 = rows["FACILITY ID"]
            data2[key2]= rows
        with open (jsonInventory, "w") as jsonf2:
            jsonf2.write(json.dumps(data2, indent = 4 ))


# Create JSON paths
csvInventory = r"Inventory_.csv"
jsonInventory = "Inventory.json"
inventory_json(csvInventory, jsonInventory)


# Translate files to JSON format - Violations file

def violation_json(csvViolations, jsonViolations):
    data3 = {}
    with open (csvViolations) as csvf3:
        csvReader = csv.DictReader(csvf3)
        for rows in csvReader: 
            key3 = rows["SERIAL NUMBER"]
            data3[key3] = rows
    with open (jsonViolations, "w") as jsonf3:
        jsonf3.write(json.dumps(data3, indent = 4))
                                   
csvViolations = r"Violations_.csv"
jsonViolations = "violations.json"
violation_json(csvViolations, jsonViolations)



