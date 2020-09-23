###get row index for all dispositions method #2
# dfs=[s32_df,slu_df,ppd_df,ptd_df]

def get_df_idx(dfs):
  idxs=[]
  for df in dfs:
    idx=df.index
    idxs.extend(idx.to_list())
  return idxs