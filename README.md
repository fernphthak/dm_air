# dm_import_helper
Help to import serveral csv files from sepecific folders and concatenate into a single `pd.DataFrame`.
# How to import
* Method1: Place `read_aqi.py` into `helpers` folder in your working directory **(Suggested)**
```python3
from helpers import read_aqi as rd
```
* Method2: Place `read_aqi.py` in your working directory
```python3
import read_aqi as rd
```
# How to use
* For example, if we want to import data from `./some_data` and make a dataframe called `A`
```python3
A=rd.read_aqi("./some_data")
```
* To get every folders' names
```python3
rd.get_dirnames()
```

* To fix time format for **'UPDATETIME'**
```python
from datetime import datetime,timedelta
from datetime import timedelta
# fix time format
def timetodt(TIME):
    try:
        try:
            return pd.to_datetime(TIME, format='%d-%m月-%y %I.%M.%S.%f000 上午')
        except ValueError:
            return pd.to_datetime(TIME, format='%d-%m月-%y %I.%M.%S.%f000 下午') + timedelta(hours=12)
    except ValueError:
        try:
            return pd.to_datetime(TIME, format='%d-%m月 -%y %I.%M.%S.%f000 上午')
        except ValueError:
            return pd.to_datetime(TIME, format='%d-%m月 -%y %I.%M.%S.%f000 下午') + timedelta(hours=12)
        # print(TIME,"is not a right format",sep=' ')

def time_fix(TABLE):
    TABLE['UPDATETIME'] = TABLE['UPDATETIME'].apply(timetodt)

time_fix("TABLENAME") # eg. aqi_2014
```
Update: please use ``pd.to_datetime`` instead of ``datetime.datetime.strptime`` since the last one contain bugs when trying to use it second time in a code.

* to fix date format for **'DATACREATIONTIME'**
```python
# fix date format
def datetodt(DATE):
    try:
        return pd.to_datetime(DATE, format='%d-%m月-%y')
    except ValueError:
        return pd.to_datetime(DATE, format='%d-%m月 -%y')
    # print(TIME,"is not a right format",sep=' ')

def date_fix(TABLE):
    TABLE['DATACREATIONDATE'] = TABLE['DATACREATIONDATE'].apply(datetodt)

date_fix("TABLENAME") # eg. aqi_2014
```