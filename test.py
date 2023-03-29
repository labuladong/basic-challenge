import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))


df.head()


df['J'] = 'alan'


df['J'].dtype=='object'



pd.Categorical(df['J'], ['clan', 'blan'])

pd.read_csv()


df.loc[:,'B'] = 232

df
