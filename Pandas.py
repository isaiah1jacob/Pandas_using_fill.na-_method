import pandas as pd
import numpy as np

df = pd.DataFrame({'new_val': [np.nan, np.nan, np.nan, np.nan]})
df['new_val'] = df['new_val'].fillna(0)

print (df)
