# get index of rows where column value is not a digit and replace with another value
def not_num_replace(df,col,replaceval=int):
  zip_str_idx = df[~(df[col].str.isdigit())].index
  df.loc[zip_str_idx,[col]]=replaceval
  return df