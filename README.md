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

* To fix time format
```python3
from datetime import datetime,timedelta
# fix time format
def timetodt(TIME):
    try:
        try:
            return datetime.strptime(TIME, '%d-%m月-%y %I.%M.%S.%f000 上午')
        except ValueError:
            return datetime.strptime(TIME, '%d-%m月-%y %I.%M.%S.%f000 下午') + timedelta(hours=12)
    except ValueError:
        try:
            return datetime.strptime(TIME, '%d-%m月 -%y %I.%M.%S.%f000 上午')
        except ValueError:
            return datetime.strptime(TIME, '%d-%m月 -%y %I.%M.%S.%f000 下午') + timedelta(hours=12)
        # print(TIME,"is not a right format",sep=' ')

def time_fix_loop(TABLE):
    TABLE['UPDATETIME'] = TABLE['UPDATETIME'].apply(lambda a: timetodt(a))

time_fix_loop("TABLENAME") # eg. aqi_2014
```