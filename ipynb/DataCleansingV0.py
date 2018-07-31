import pandas as pd

fn=input("filename?")
fnn=fn+".csv"
print(fnn)
df = pd.read_csv(fnn)
df.columns = ['year', 'rank', 'company', 'revenue', 'profit']
print(len(df))
print(df.dtypes)

if(df.profit.dtype=='object'):
   non_numberic_profits = df.profit.str.contains('[^0-9.-]')
   print(df.loc[non_numberic_profits].head())
   print(df.loc[non_numberic_profits].tail())

   print(set(df.profit[non_numberic_profits]))
   print(len(df.profit[non_numberic_profits]))

   df = df.loc[~non_numberic_profits]
   df.profit = df.profit.apply(pd.to_numeric)
   print("non-numeric profits are removed. New length and data types:")
   print(len(df))
   print(df.dtypes)
else:
    print("All profits are numeric. No changes in length and data types:")

