import pandas as pd
import numpy as np

td = pd.DataFrame({'column': np.empty((1000000))})

for i in range(100):
    td.column = np.sqrt(td.column)
