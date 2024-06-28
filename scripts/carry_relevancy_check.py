# ****************************************
# Confounder Handling Simulation Study
# 
# Carry through relevancy checks from existing lit review when base collection changes
# 
# Emma Tarmey
#
# Started:          28/06/2024
# Most Recent Edit: 28/06/2024
# ****************************************


import sys
import numpy as np
import pandas as pd


new_sources_filename   = "../results/all_sources.csv"
old_relevancy_filename = "../results/all_sources_manual_review_linked.csv"

new_sources_df = pd.read_csv(new_sources_filename)
print(new_sources_df.columns)
print(new_sources_df.head)

old_relevancy_df = pd.read_csv(old_relevancy_filename)
old_relevancy_df = old_relevancy_df[['DOI', 'Relevant_methods', 'Relevant_simulation', 'Review_paper', 'Notes']]
print(old_relevancy_df.columns)
print(old_relevancy_df.head)

union = pd.merge(new_sources_df, old_relevancy_df, how = "outer", on='DOI')
union.rename(columns={'Notes':'Emma_Notes'}, inplace=True)
num_papers = len(union.index)
union['Kate_Notes']     = ["" for x in range(num_papers)]
union['Jonathan_Notes'] = ["" for x in range(num_papers)]
union['Rhian_Notes']    = ["" for x in range(num_papers)]
union['Paul_Notes']     = ["" for x in range(num_papers)]
print(union.columns)
print(union.head)
union.to_csv('../results/all_sources_manual_review_linked_carried.csv', index=False)


