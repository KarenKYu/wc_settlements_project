import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from wc_settlement_all import add_claim_resolution_cols, add_disposition_labels,\
 coerce_cols_to_datetime, days_diff_datetime_cols, replace_missing_accid_date,\
     drop_unneccessary_cols, clean_cols

# only read in first 100000 rs == 2% of total dataset rows from WC Dataset
df=pd.read_csv('./data/Assembled_Workers__Compensation_Claims___Beginning_2000.csv', nrows=100000)

df_with_resolution_cols = add_claim_resolution_cols(df)

comb_disp_df = add_disposition_labels(df_with_resolution_cols)

comb_disp_df = coerce_cols_to_datetime(comb_disp_df)

diff_df = days_diff_datetime_cols(comb_disp_df)

# diff_df.to_csv('diff_df.csv')

clean_df =  clean_cols(diff_df)

scoped_df = drop_unneccessary_cols(clean_df)

scoped_df.to_csv("scoped_df.csv", index=False)

