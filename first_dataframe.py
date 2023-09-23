import pandas as pd
import numpy as np

data = {
    "id":np.array([1,2,3,4]),
    "name":np.array(['A', 'B', 'C', 'D']),
    "age":np.array([28,29,30,31])
}

df = pd.DataFrame(data)
print(df.info())