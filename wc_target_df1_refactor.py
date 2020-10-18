import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# only read in first 100000 rows == 2% of total dataset rows from WC Dataset
df=pd.read_csv('./data/Assembled_Workers__Compensation_Claims___Beginning_2000.csv', nrows=100000)

### Create target by combining the 4 types of final WC claim dispositions into one column

# Create a Final disposition column to use as target- combines all final disposition classes into one column
# Create a Final disposition date column - combines all final disposition dates into one column
# Create a Days_Accid_Final column = days claim opened from date of accident to final disposition date
# Create a Days_Assemb_Final column = days claim opened from date of assembly to final disposition date

from wc_settlement_all import add_cols_df, combine_disp_cols

# created new dataframe with 4 new columns
new_cols=['Final_disposition', 'Final_disposition_Date', 'Days_Accid_Final', 'Days_Assemb_Final']

disp_df = add_cols_df(df, new_cols)

# gets all rows with a certain type of final disposition that is not null and adds the disposition date to new col and type of disposition 
# string to Final Disposition
final_disps = [('PPD Non-Scheduled Loss Date','PPD'),('PPD Scheduled Loss Date', 'SLU'),
			   ('Section 32 Date', 'S32'),('PTD Date', 'PTD')]

additional_dfs = [combine_disp_cols(disp_df, disp_date, disp_name) for disp_date,disp_name in final_disps]

# combine original df with ppd_df,slu_df,s32_df and ptd_df
comb_disp_df = pd.concat(additional_dfs,ignore_index=True,axis=0)

#Coerce dates to datetime

# find all column names with word Date and Days and coerce to datetime
date='Date'
day='Days'

dates=[name for name in comb_disp_df.columns if date in name]
days = [name for name in comb_disp_df.columns if day in name]

date_names = dates+days

comb_disp_df[date_names]=comb_disp_df[date_names].apply(pd.to_datetime,errors='coerce')

# find difference in days from two datetime column values

comb_disp_df['Days_Accid_Final']=comb_disp_df['Final_disposition_Date']-comb_disp_df['Accident Date']
comb_disp_df['Days_Assemb_Final']=comb_disp_df['Final_disposition_Date']-comb_disp_df['Assembly Date']

# Getting the integer portion of the timedelta to get # of days
comb_disp_df['Days_Accid_Final']=comb_disp_df['Days_Accid_Final'].dt.days
comb_disp_df['Days_Assemb_Final']=comb_disp_df['Days_Assemb_Final'].dt.days

### Select only rows with final dispositions
final_df= comb_disp_df[comb_disp_df['Final_disposition'].notnull()]
# final_df.shape
# (16509, 56)

#save to csv file
final_df.to_csv("final_df.csv", index=False)

