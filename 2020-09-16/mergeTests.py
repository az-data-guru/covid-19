import time
import datetime
import pandas as pd

counties= ["ARIZONA","APACHE","YUMA","YAVAPAI","SANTA_CRUZ","PINAL","PIMA","NAVAJO","MOHAVE","MARICOPA","LA_PAZ","GREENLEE","GRAHAM","GILA","COCONINO","COCHISE"]
from datetime import date
today = date.today()
yesterday = today - datetime.timedelta(days=1)
yesterday.isoformat() 

for county in counties:
    filein=f"F:/OneDrive/OneDrive - The E.W. Scripps Company/R Projects/Hospital-Referral-Region-graphic/covid/Data/2020-09-16/countyTests{yesterday.isoformat()}-{county}.csv"
    df = pd.read_csv(filein)
    if counties[0] == county:
        dfm=df
    else:
        dfm=pd.merge(dfm,df,on='date',how = 'outer')


fileout=f"AllTests{yesterday.isoformat()}.csv"
dfm.to_csv(fileout, index=False)

