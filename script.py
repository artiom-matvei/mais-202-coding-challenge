#python version used 2.7.14
#pandas version used 0.23.4
#numpy version used 1.15.4
#numpy version used 2.2.3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv ('data.csv')
dfgrouped=df.groupby(['purpose'])
smdf = dfgrouped.mean()[['int_rate']]
ax = smdf.plot(kind='bar',legend=True, figsize=(15,10), fontsize=9, rot=20)
plt.show()
