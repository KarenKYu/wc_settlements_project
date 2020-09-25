import pandas as pd
import numpy as np
import re
def add_datepart(df, colname, drop=True, time=False, errors="raise"):
    col = df[colname]
    col_dtype = col.dtype
    if isinstance(col_dtype, pd.core.dtypes.dtypes.DatetimeTZDtype):
        col_dtype = np.datetime64

    if not np.issubdtype(col_dtype, np.datetime64):
        df[colname] = col = pd.to_datetime(col, infer_datetime_format=True, errors=errors)
    targ_pre = re.sub('[Dd]ate$', '', colname)
    attr = ['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
            'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start', 'Is_year_end', 'Is_year_start']
    if time: attr = attr + ['Hour', 'Minute', 'Second']
    for n in attr: df[targ_pre + n] = getattr(col.dt, n.lower())
    df[targ_pre + 'Elapsed'] = col.astype(np.int64) // 10 ** 9
    if drop: df.drop(colname, axis=1, inplace=True)
