""" You have to import these before using this helpers
import os
import pandas as pd
"""

def read_aqi(DIRNAME):
    for root, dirs, files in os.walk(DIRNAME, topdown=False):
        input=pd.DataFrame()
        for name in files:
            input=pd.concat([input,pd.read_csv(os.path.join(root, name),encoding='big5')])
            print("Reading",os.path.join(root, name),sep= ' ',end='\n')
        return input


""" Example:
input=read_aqi("../EPA_ERDB_2015")
print(input)
"""