import os
import pandas as pd
from datetime import datetime

# core operation
def read_aqi(DIRNAME):
    print("Start importing files from", DIRNAME, sep=' ',end='\n')
    for root, dirs, files in os.walk(DIRNAME, topdown=False):
        output=pd.DataFrame()
        for name in files:
            output=pd.concat([output,pd.read_csv(os.path.join(root, name),encoding='big5')])
            print("Reading",os.path.join(root, name),sep= ' ',end='\n')
    print("Done importing files from", DIRNAME, sep=' ',end='\n')
    return output.reset_index()

# print all folder names in the current directory
def get_dirnames():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            print(os.path.join(root, name))

# print all filenames in the given folder
def get_filenames(DIRNAME):
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))

# fix time format
def timetodt(TIME):
    try:
        return datetime.strptime(TIME, '%d-%m月-%y %I.%M.%S.%f000 上午')
    except ValueError:
        try:
            return datetime.strptime(TIME, '%d-%m月-%y %I.%M.%S.%f000 下午')
        except ValueError:
            print(TIME,"is not a right format",sep=' ')