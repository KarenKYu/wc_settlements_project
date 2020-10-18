
import pandas as pd
import numpy as np
import pdb

# remove comma and replace Nan values with zero and cast as new datatype
def type_col(df,col,typecast):
    df[col]=df[col].str.replace(',', '').replace('-','').replace(np.NaN,0).replace([None],0).astype(typecast)
    return df

# remove asterisk from oiics code columns, replace Nan with zero, and cast all as type integer

def strip_char(code,char='*'):
  clean = code.str.strip(char)
  return clean


# Get list of OIICS Code columns remove asterisk from values, replace Nan with zero, and cast all as type integer
def clean_ooics_codes(df,cols):
  return df[cols].apply(strip_char).fillna(0).astype('int')


  # Create a Final disposition column to use as target- combines all final disposition classes into one column
# Create a Final disposition date column - combines all final disposition dates into one column
# Create a Days_Accid_Final column = days claim opened from date of accident to final disposition date
# Create a Days_Assemb_Final column = days claim opened from date of assembly to final disposition date

# add 4 new columns to combine data
# Final disposition == type of closing/settlement: ex. S-32, SLU, Non-SLU PPD, PTD
# Final disposition date == date of closing/settlement
# Days Accid Final == # of days from accident date to date of final disposition date
# Days Assemb Final == # of days from WCB Assembly of claim date to date of final disposition date

def add_cols_df(df, new_cols):
  orig_cols=df.columns.tolist()
  cols=orig_cols+new_cols
  disp_df = df.reindex(columns=cols)
  return disp_df

#['Section 32 Date', 'PPD Scheduled Loss Date', 'PPD Non-Scheduled Loss Date', 'PTD Date']
# # slu_df = disp_df[disp_df['PPD Scheduled Loss Date'].notnull()]
# copy slu disposition dates to final disposition date column
# # slu_df['Final_disposition_date']=slu_df['PPD Scheduled Loss Date']
# # slu_df['Final_disposition']='SLU'

# gets all rows with a certain type of final disposition that is not null and adds the disposition date to new col and type of disposition 
# string to Final Disposition
def combine_disp_cols(df, disp_date, disp_name):
  select_df = df[df[disp_date].notnull()]
  select_df['Final_disposition_Date']=select_df[disp_date]
  select_df['Final_disposition']=disp_name
  return select_df

# get index of rows where column value is not a digit and replace with another value
def not_num_replace(df,col,replaceval=int):
  zip_str_idx = df[~(df[col].str.isdigit())].index
  df.loc[zip_str_idx,[col]]=replaceval
  return df

  # removes commas and dashes, replaces None with 0, especially for AWW column
def type_col(df,col,typecast):
  df[col]=df[col].str.replace(',', '').replace('-','').replace([None],0).astype(typecast)
  return df

def clean_zip(col):
  return pd.to_numeric(col, errors='coerce',downcast='signed')
  
  