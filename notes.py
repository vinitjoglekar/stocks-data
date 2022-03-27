'''
NSE series legends
Fully paid equity shares/ETFs   EQ, BE, BZ
Rigths Entitlements             BE
Partly paid equity shares       E@, X@; where @ = 1-9, A-Z
Refer: https://www.nseindia.com/market-data/legend-of-series
'''

import pandas as pd
df = pd.read_csv('NSE-2017-2021.csv')

df.head(5)
df.SERIES.unique()
df.SERIES.nunique(dropna = True)
df[df.SERIES=="BZ"].head(5)

len(df)
df_eq = df[df.SERIES.isin(['EQ','BE','BZ','E1','E2','E3','X1','X2','X3'])]
symbols = df_eq.SYMBOL.unique()

df_reliance=df[df.SYMBOL == 'RELIANCE']


