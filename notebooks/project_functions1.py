import pandas as pd
import numpy as np
import ast
import operator
from functools import reduce

def load_and_process(url_or_path_to_csv_file):
    def get_number(lib):
        num = 0
        for n in range(0, 1000):
             if lib.get(n) is not None:
                num+=1
        return num
    df1=(
    pd.read_csv(url_or_path_to_csv_file)
    .drop(["gameId","gameDuration","level","lastRound","ingameDuration",'combination'], axis="columns")
    .loc[lambda x: x['Ranked']==1]
    .reset_index()
    .drop(["index"], axis="columns")
    .assign(champion_dict=lambda df:
            df['champion'].apply(lambda x: ast.literal_eval(x)))
    .drop(["champion"], axis="columns")
    )
    clist=list(np.unique(reduce(operator.add, df1.champion_dict.apply(lambda x: list(x.keys())))))
    
    df2=df1.join([ pd.DataFrame(None, index=df1.index, columns=sorted(clist) )])
        

    for i in range(len(df2.champion_dict)):
        keylist=list(df2.champion_dict[i].keys())
        for k in clist:
            value=df2.champion_dict[i].get(k)
            df2.at[i,k]=value
    df2.head()
    d_ahri = df2.get('Ahri')
    d_annie = df2.get('Annie')
    d_ashe = df2.get('Ashe')
    d_aurelionsol = df2.get('AurelionSol')
    d_blitzcrank = df2.get('Blitzcrank')
    d_caitlyn = df2.get('Caitlyn')
    d_chogath = df2.get('ChoGath')
    d_darius = df2.get('Darius')
    d_ekko = df2.get('Ekko')
    d_ezreal = df2.get('Ezreal')
    d_fiora = df2.get('Fiora')
    d_fizz = df2.get('Fizz')
    d_gangplank = df2.get('Gangplank')
    d_graves = df2.get('Graves')
    d_irelia = df2.get('Irelia')
    d_jarvaniv = df2.get('JarvanIV')
    d_jayce = df2.get('Jayce')
    d_jhin = df2.get('Jhin')
    d_jinx = df2.get('Jinx')
    d_kaisa = df2.get('KaiSa')
    d_karma = df2.get('Karma')
    d_kassadin = df2.get('Kassadin')
    d_kayle = df2.get('Kayle')
    d_khazix = df2.get('KhaZix')
    d_leona = df2.get('Leona')
    d_lucian = df2.get('Lucian')
    d_lulu = df2.get('Lulu')
    d_lux = df2.get('Lux')
    d_malphite = df2.get('Malphite')
    d_masteryi = df2.get('MasterYi')
    d_missfortune = df2.get('MissFortune')
    d_mordekaiser = df2.get('Mordekaiser')
    d_neeko = df2.get('Neeko')
    d_poppy = df2.get('Poppy')
    d_rakan = df2.get('Rakan')
    d_rumble = df2.get('Rumble')
    d_shaco = df2.get('Shaco')
    d_shen = df2.get('Shen')
    d_sona = df2.get('Sona')
    d_soraka = df2.get('Soraka')
    d_syndra = df2.get('Syndra')
    d_thresh = df2.get('Thresh')
    d_twistedfate = df2.get('TwistedFate')
    d_velkoz = df2.get('VelKoz')
    d_vi = df2.get('Vi')
    d_wukong = df2.get('WuKong')
    d_xayah = df2.get('Xayah')
    d_xerath = df2.get('Xerath')
    d_xinzhao = df2.get('XinZhao')
    d_yasuo = df2.get('Yasuo')
    d_ziggs = df2.get('Ziggs')
    d_zoe = df2.get('Zoe')
    finaldf = (pd.DataFrame.from_dict({'champions': ['Ahri','Annie', 'Ashe', 'AurelionSol', 'Blitzcrank', 'Caitlyn', 'ChoGath', 'Darius', 'Ekko', 'Ezreal', 'Fiora',
                              'Fizz', 'Gangplank', 'Graves', 'Irelia', 'JarvanIV', 'Jayce', 'Jhin', 'Jinx', 'KaiSa', 'Karma', 'Kassadin', 'Kayle', 
                              'KhaZix', 'Leona', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'MasterYi', 'MissFortune', 'Mordekaiser', 'Neeko', 'Poppy', 
                              'Rakan', 'Rumble', 'Shaco', 'Shen', 'Sona', 'Soraka', 'Syndra', 'Thresh', 'TwistedFate', 'VelKoz', 'Vi', 'WuKong', 
                              'Xayah', 'Xerath', 'XinZhao', 'Yasuo', 'Ziggs', 'Zoe'], 
                 'used_frequence':[get_number(d_ahri),get_number(d_annie), get_number(d_ashe), get_number(d_aurelionsol), get_number(d_blitzcrank), 
                                  get_number(d_caitlyn), get_number(d_chogath), get_number(d_darius),get_number(d_ekko), get_number(d_ezreal), 
                                  get_number(d_fiora), get_number(d_fizz), get_number(d_gangplank), get_number(d_graves), get_number(d_irelia), 
                                  get_number(d_jarvaniv), get_number(d_jayce), get_number(d_jhin), get_number(d_jinx), get_number(d_kaisa), 
                                  get_number(d_karma), get_number(d_kassadin), get_number(d_kayle), get_number(d_khazix), get_number(d_leona), 
                                  get_number(d_lucian), get_number(d_lulu), get_number(d_lux), get_number(d_malphite), get_number(d_masteryi), 
                                  get_number(d_missfortune), get_number(d_mordekaiser), get_number(d_neeko), get_number(d_poppy), get_number(d_rakan),
                                  get_number(d_rumble), get_number(d_shaco), get_number(d_shen), get_number(d_sona), get_number(d_soraka), 
                                  get_number(d_syndra), get_number(d_thresh), get_number(d_twistedfate), get_number(d_velkoz), get_number(d_vi), 
                                  get_number(d_wukong), get_number(d_xayah), get_number(d_xerath), get_number(d_xinzhao), get_number(d_yasuo), 
                                  get_number(d_ziggs), get_number(d_zoe)]})
         .sort_values('used_frequence', ascending = False)
        )
    
    return finaldf