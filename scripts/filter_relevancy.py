# ****************************************
# Confounder Handling Simulation Study
#
# Filter to only relevant papers
#
# Emma Tarmey
#
# Started:          28/06/2024
# Most Recent Edit: 28/06/2024
# ****************************************

import sys
import numpy as np
import pandas as pd

filename = "../results/all_sources_manual_review_linked_carried.csv"

df = pd.read_csv(filename)
print(df.columns)
print(df.head)

relevancy_score = df['Relevant_methods'] + df['Relevant_simulation'] + df['Review_paper']
df['relevancy'] = relevancy_score
relevant_df     = df.loc[df['relevancy'] > 0]
print(relevant_df.columns)
print(relevant_df.head)
relevant_df.to_csv('../results/all_sources_manual_review_linked_carried_relevant.csv', index=False)

