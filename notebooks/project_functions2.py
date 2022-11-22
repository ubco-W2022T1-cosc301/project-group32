

def load_and_process(url_or_path_to_csv_file):
    import pandas as pd
    import numpy as np
    import ast
    import operator
    from functools import reduce
    #method1 chain: delete unnessesary columns, delete rows that rank not euqal to 1, convert 'combination' column to string list and add it to new list, drop 'combination' column
    df1=(
    pd.read_csv(url_or_path_to_csv_file)
    .drop(["gameId","gameDuration","level","lastRound","ingameDuration",'champion'], axis="columns")
    .loc[lambda x: x['Ranked']==1]
    .reset_index()
    .drop(["index"], axis="columns")
    .assign(combination_dict=lambda df:
            df['combination'].apply(lambda x: ast.literal_eval(x)))
    .drop(["combination"], axis="columns")
    )
    clist=list(np.unique(reduce(operator.add, df1.combination_dict.apply(lambda x: list(x.keys())))))
    
    #method2 chain create empty column for all unique 
    df2=df1.join([ pd.DataFrame(None, index=df1.index, columns=sorted(clist) )])
        

    for i in range(len(df2.combination_dict)):
        keylist=list(df2.combination_dict[i].keys())
        for k in clist:
            value=df2.combination_dict[i].get(k)
            df2.at[i,k]=value
    fdf=pd.DataFrame(columns=clist,index=[0,1,2,3,4,5,6,7,8,9])    
    for col in fdf:
        d=dict(df2[col].value_counts())
        for key,value in d.items():
            fdf.at[key,col]=value  
    
    fdf=fdf.transpose()
    return fdf 
