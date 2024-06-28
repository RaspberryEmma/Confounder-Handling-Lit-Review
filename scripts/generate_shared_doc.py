# ****************************************
# Confounder Handling Simulation Study
#
# Reproducible Literature Review - Generate shared document template
#
# Emma Tarmey
#
# Started:          28/06/2024
# Most Recent Edit: 28/06/2024
# ****************************************

import pandas as pd
import sys

relevant_filename = "../results/all_sources_manual_review_linked.csv"
df = pd.read_csv(relevant_filename, delimiter=',')
relevancy_score = df['Relevant_methods'] + df['Relevant_simulation'] + df['Review_paper']
df['relevancy'] = relevancy_score
relevant_df = df.loc[df['relevancy'] > 0]

verbose_filename = "../results/all_sources.csv"
verbose_df       = pd.read_csv(verbose_filename, delimiter=',')

# display everything
pd.set_option('display.max_colwidth', 150)

print("\n\n*** Relevant Papers ***")
print(relevant_df.columns)
print(relevant_df.head)
#sys.exit("Stop here please")

print("\n\n*** All Papers ***")
print(verbose_df.columns)
print(verbose_df.head)

