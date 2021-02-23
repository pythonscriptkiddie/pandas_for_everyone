import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')

print(df.head())
print(type(df))
print(df.shape)
print(df.columns)
print(df.info())