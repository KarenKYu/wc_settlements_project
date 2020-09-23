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
  orig_cols=df.columns.to_list()
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
def combine_disposition_cols(df, date_col, combdate_col='Final_disposition_Date', disp_word_col='Final_disposition', disp_word='str'):
  select_df = df[df[date_col].notnull()]
  select_df[combdate_col]=select_df[date_col]
  select_df[disp_word_col]=disp_word
  return select_df

