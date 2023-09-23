import pandas as pd
all_movies = pd.read_csv('Hydra-Movie-Scrape.csv')
description = all_movies.head(1)
for x in list(description):
    print(description.at[0,x])