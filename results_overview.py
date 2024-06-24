# ****************************************
# Confounder Handling Simulation Study
#
# Reproducible Literature Review - Overview of results
#
# Emma Tarmey
#
# Started:          13/06/2024
# Most Recent Edit: 13/06/2024
# ****************************************

import sys
import numpy as np
import pandas as pd

filename = "results/all_sources_manual_review_linked.csv"
df = pd.read_csv(filename, delimiter=',')
relevancy_score = df['Relevant_methods'] + df['Relevant_simulation'] + df['Review_paper']
df['relevancy'] = relevancy_score

relevant_df = df.loc[df['relevancy'] > 0]
methods_df = df.loc[df['Relevant_methods'] == 1]
sim_df     = df.loc[df['Relevant_simulation'] == 1]
review_df  = df.loc[df['Review_paper'] == 1]
best_df    = df.loc[df['relevancy'] == 3]

# display everything
pd.set_option('display.max_colwidth', 150)

print("\n\n*** All Papers ***")
print(df)
print("\n\n*** Relevant Papers ***")
print(relevant_df)
print("\n\n*** Relevant Methods Papers ***")
print(methods_df)
print("\n\n*** Relevant Simulation Papers ***")
print(sim_df)
print("\n\n*** Relevant Review Papers ***")
print(review_df)
print("\n\n*** Relevant Best Papers ***")
print(best_df)

