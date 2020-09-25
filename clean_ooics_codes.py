# Get list of OIICS Code columns remove asterisk from values, replace Nan with zero, and cast all as type integer
def clean_ooics_codes(df,cols):
  df[cols]= df[cols].apply(strip_char).replace(np.NaN,0).astype('int')
  return df