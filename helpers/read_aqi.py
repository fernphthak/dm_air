import os
import pandas as pd

# core operation
def read_aqi(DIRNAME):
    print("Start importing files from", DIRNAME, sep=' ',end='\n')
    for root, dirs, files in os.walk(DIRNAME, topdown=False):
        input=pd.DataFrame()
        for name in files:
            input=pd.concat([input,pd.read_csv(os.path.join(root, name),encoding='big5')])
            print("Reading",os.path.join(root, name),sep= ' ',end='\n')
    print("Done importing files from", DIRNAME, sep=' ',end='\n')
    return input

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


""" Example:
input=read_aqi("../EPA_ERDB_2015")
print(input)
"""