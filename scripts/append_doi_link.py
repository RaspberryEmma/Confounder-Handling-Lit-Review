# ****************************************
# Confounder Handling Simulation Study
# 
# Change DOI to DOI Link
# 
# Emma Tarmey
#
# Started:          03/06/2024
# Most Recent Edit: 03/06/2024
# ****************************************


import sys
import numpy as np
import pandas as pd


filename  = "../results/all_sources_manual_review.csv"
doi_start = "https://doi.org/"

df = pd.read_csv(filename)
print(df)
print(df.columns)
print(df['DOI'])

doi_links = doi_start + df['DOI'].astype(str)
print(doi_links)
df['DOI'] = doi_links

df.to_csv('../results/all_sources_manual_review_linked.csv', index=False)


