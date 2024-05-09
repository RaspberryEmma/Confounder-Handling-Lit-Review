# ****************************************
# Confounder Handling Simulation Study
# 
# Reproducible Literature Review - Records Processing
# 
# Emma Tarmey
#
# Started:          07/05/2024
# Most Recent Edit: 09/05/2024
# ****************************************


import pandas as pd
import numpy as np


web_of_science_filename = "results/web_of_science.txt" # note: tab delimited, not csv
pubmed_filename         = "results/pubmed.csv"
key_papers_filename     = "results/key_papers.csv"


print("\n\n*** Web of Science ***")
web_of_science_df = pd.read_csv(web_of_science_filename, delimiter='\t')
web_of_science_df = web_of_science_df[["TI", "DI"]]
web_of_science_df.rename(columns={'TI':'Title', 'DI':'DOI'}, inplace=True)
web_of_science_df = web_of_science_df.replace('NaN', np.nan)
web_of_science_df = web_of_science_df.dropna()
print(web_of_science_df)


print("\n\n*** PubMed ***")
pubmed_df = pd.read_csv(pubmed_filename)
pubmed_df = pubmed_df[["Title", "DOI"]]
pubmed_df = pubmed_df.replace('NaN', np.nan)
pubmed_df = pubmed_df.dropna()
print(pubmed_df)


print("\n\n*** Union ***")
union = pd.merge(web_of_science_df, pubmed_df, how = "outer", on='DOI')
print(union)
union.to_csv('results/all_sources.csv', index=False)


print("\n\n*** Key Papers ***")
key_papers_df = pd.read_csv(key_papers_filename)
key_papers_df.loc[:, "DOI"] = (key_papers_df.loc[:, "DOI"].str.split('.org/').str[1])
key_papers_df = key_papers_df[["Title", "DOI"]]
print(key_papers_df)


print("\n\n *** Summary ***")
print("Web of Science, n =", len(web_of_science_df.index))
print("PubMed, n =", len(pubmed_df.index))
print("Union, n =", len(union.index))


print("\n\n")
print(union["DOI"])
print("\n")
print(key_papers_df["DOI"])


found = False
for i in range(0, len(key_papers_df["DOI"])):
    found = False
    paper = (key_papers_df.loc[:, "Title"])[i]
    doi   = (key_papers_df.loc[:, "DOI"])[i]

    if doi in union["DOI"]:
        found = True

    print("  *", paper, ":", found)

