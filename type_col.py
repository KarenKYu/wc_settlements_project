# removes commas and dashes, replaces None with 0, especially for AWW column
def type_col(df,col,typecast):
  df[col]=df[col].str.replace(',', '').replace('-','').replace([None],0).astype(typecast)
  return df