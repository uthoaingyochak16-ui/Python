import pandas as pd 

# df=pd.read_json(r'C:\Users\Uthoaingyo\Python\pandas\sample_Data.json')
# print(df.info())

df=pd.read_csv(r'C:\Users\Uthoaingyo\Python\pandas\sales_data_sample.csv',encoding='latin1')
print(df.shape)
# print(df.columns)

hdf=df.head(20)
print(hdf[(hdf['QUANTITYORDERED']>40) | (hdf['PRICEEACH']>99)])

tdf=df.tail(20)
# print(tdf['CUSTOMERNAME'])