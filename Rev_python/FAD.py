import numpy as np
import pandas as pd
rand_arr = np.random.rand(30,5)
df = pd.DataFrame(rand_arr, columns=['A', 'B', 'C', 'D','E'])
print(df) 
average_prices = df.mean()
print(average_prices)
print(max(average_prices))
df_normalized = (df - df.min()) / (df.max() - df.min())
print(df_normalized)
risky_investment = df.lt(200).any(axis=1)
df['Risk_Flag'] = np.where(risky_investment, '⚠️ Risky Investment', '')