

def load_and_process(url_or_path_to_csv_file):
    import numpy as np
    import pandas as pd
    import matplotlib.pylab as plt
    import seaborn as sns
    import ast

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .dropna()
        .drop(["gameDuration","level","lastRound","ingameDuration"], axis="columns")
        .loc[lambda x: x['Ranked']==1]
        .reset_index()
        .drop(["index"], axis="columns")
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        
        df1
        .assign(items_dict=lambda df:
            df['champion'].apply(lambda x: ast.literal_eval(x)))
        .drop(["champion"], axis="columns")

      )

    # Make sure to return the latest dataframe

    return df2 
