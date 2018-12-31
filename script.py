import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv ('/home/artiom/Code/mais-202-coding-challenge/data.csv')
df = pd.read_csv ('data.csv')
dfgrouped=df.groupby(['purpose'])
smdf = dfgrouped.mean()[['int_rate']]
ax = smdf.plot(kind='bar',legend=True, figsize=(15,10), fontsize=9, rot=20)
plt.show()
