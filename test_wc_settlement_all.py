import pandas as pd
from wc_settlement_all import strip_char, remove_asterisks_commas, add_claim_resolution_cols, combine_disp_cols, add_disposition_labels

def test_strip_char():
    s = pd.Series(['*89', '*1',',67'])
    num_ser = ['89','1','67']
    assert strip_char(s).tolist() == num_ser

def test_remove_asterisks_commas():
    data = {'a':['*45'],'b':['90*'],'c':['*76'],'d':['77*'],'e':['*88']}
    df = pd.DataFrame(data)
    cols= ['OIICS Part Of Body Code','OIICS Nature of Injury Code','OIICS Injury Source Code','OIICS Event Exposure Code',
                   'OIICS Secondary Source Code']
    df.columns = cols
    clean_df = remove_asterisks_commas(df)
    assert clean_df.iloc[:,0].tolist() == ['45']
    assert clean_df.iloc[:,1].tolist() == ['90']

df = pd.read_csv('sample_df.csv')

def test_add_claim_resolution_cols():
    new_cols=['Final_disposition', 'Final_disposition_Date', 'Days_Accid_Final', 'Days_Assemb_Final']
    orig_cols=df.columns.tolist()
    cols=new_cols+orig_cols
    assert sorted(add_claim_resolution_cols(df).columns.tolist()) == sorted(cols)

res_df = pd.read_csv('sample_res_df.csv')
ppd_df = pd.read_csv('ppd_df.csv')

def test_combine_disp_cols():
    disp_date = 'PPD Non-Scheduled Loss Date'
    disp_name = 'PPD'
    select_df = res_df[res_df[disp_date].notnull()]
    select_df['Final_disposition_Date']=select_df[disp_date]
    select_df['Final_disposition']=disp_name
    assert combine_disp_cols(res_df, disp_date, disp_name).sort_index(inplace=True) == ppd_df.sort_index(inplace=True)

pre_concat_df = pd.read_csv('pre_concat_df.csv')
concat_df = pd.read_csv('concat_df.csv')

def test_add_disposition_labels():
    assert add_disposition_labels(pre_concat_df).sort_index(inplace=True) == concat_df.sort_index(inplace=True)


