import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df0=pd.read_excel(r"C:\Users\Uthoaingyo\Python\Movie.xlsx",)

df=df0.head(20)
pd.DataFrame(df)
# df_filter=df[]
print(df[['title','imdb_score']])