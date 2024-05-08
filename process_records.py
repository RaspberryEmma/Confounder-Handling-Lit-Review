# ****************************************
# Confounder Handling Simulation Study
# 
# Reproducible Literature Review - Records Processing
# 
# Emma Tarmey
#
# Started:          08/05/2024
# Most Recent Edit: 08/05/2024
# ****************************************

#import os as os
import pandas as pd
import numpy as np

web_of_science_filename = "results/web_of_science.txt" # note: tab delimited, not csv
pubmed_filename         = "results/pubmed.csv"
zoterro_filename        = "results/zoterro.csv"

print("\n\n*** Web of Science ***")
web_of_science_df = pd.read_csv(web_of_science_filename, delimiter='\t')
web_of_science_df = web_of_science_df[["TI", "DI"]]
web_of_science_df.rename(columns={'TI':'Title', 'DI':'DOI'}, inplace=True)
print(web_of_science_df)

print("\n\n*** PubMed ***")
pubmed_df = pd.read_csv(pubmed_filename)
pubmed_df = pubmed_df[["Title", "DOI"]]
print(pubmed_df)

print("\n\n*** Zoterro ***")
zoterro_df = pd.read_csv(zoterro_filename)
zoterro_df.loc[:, "DOI"] = (zoterro_df.loc[:, "DOI"].str.split('.org/').str[1])
zoterro_df = zoterro_df[["Title", "DOI"]]
zoterro_df = zoterro_df.replace('NaN', np.nan)
zoterro_df = zoterro_df.dropna() # NA or NaN indicates not an academic article here
print(zoterro_df)

print("\n\n*** Summary ***")
union = pd.merge(web_of_science_df, pubmed_df, on='DOI')
print(union)
union.to_csv('results/all_sources.csv', index=False)

# check whether nrow(intersection(union, zoterro) == nrow(zoterro)
intersection = pd.merge(union, zoterro_df, how ='inner', on =['DOI', 'DOI'])
print(intersection)

