#imports libraries
import numpy as np
import pandas as pd
import time
from unicodedata import normalize

#starts time counter
print("Started product classification:")
start_time = time.time()

#reads the file using pandas, separating at tabs, and saves as a dataframe
data_table = pd.read_csv('data_estag_ds.tsv', skiprows=1, names=["ID", "Name"], sep='\t', engine='python')
data_table.info()

#adds a new column to the dataframe, in order to save the classification result
data_table["Result"] = np.nan

#defines keywords that identify if the product is smartphone related
smartphone_keywords = ["smartphone", "phone", "celular", "iphone", "apple", "samsung", "asus", "motorolla", "xperia", "xiaomi", "nokia", "blackberry", "huawei", "android"]

#loops through each row and checks for keywords in the product name. if positive, classifies the product as "Smartphone Related", or else, "Non-Smartphone Related"
index = 0
sp_count = 0
nsp_count = 0
for n in data_table["Name"]:
    #tokenize the product name, removing accents and special characters, converting to lowercase and splitting at spaces and commas
    unaccented_string = normalize('NFKD', n).encode('ASCII','ignore').decode('utf-8')
    tokens = unaccented_string.casefold().split(' ')

    #substitute the product's name in the dataframe for the unnaccented one, for clarity
    data_table.loc[index, "Name"] = unaccented_string

    #check if both lists have at least one element in common
    if(set(tokens) & set(smartphone_keywords)):
        data_table.loc[index, "Result"] = "Smartphone Related"
        sp_count += 1
    else:
        data_table.loc[index, "Result"] = "Non-Smartphone Related"
        nsp_count += 1

    index += 1

#ends time counter
end_time = time.time() - start_time

print("\nClassification Results:\n")
print(data_table)
print("\nResults can also found in file 'csv_results_table.csv'")
print("\nFinished classification in " + str(end_time) + " seconds")
print("\nSmartphone related items: " + str(sp_count))
print("Non-Smartphone related items: " + str(nsp_count))

data_table.to_csv(r'csv_results_table.csv', index=None, header=True)
data_table.to_csv(r'txt_results_table.txt', index=None, header=True)