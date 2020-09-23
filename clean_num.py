# remove comma and replace Nan values with zero and cast as new datatype
from numpy import *

def type_col(df,col,typecast):
  from numpy import *
  df[col]=df[col].str.replace(',', '').replace('-','').replace(np.Nan,0).replace([None],0).astype(typecast)
  return df

# remove asterisk from oiics code columns, replace Nan with zero, and cast all as type integer

def strip_char(code,char='*'):
  clean = code.str.strip(char)
  return clean