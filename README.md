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
# fix time format
def timetodt(TIME):
    try:
        try:
            return datetime.strptime(TIME, '%d-%m月-%y %I.%M.%S.%f000 上午')
        except ValueError:
            return datetime.strptime(TIME, '%d-%m月-%y %I.%M.%S.%f000 下午')
    except ValueError:
        try:
            return datetime.strptime(TIME, '%d-%m月 -%y %I.%M.%S.%f000 上午')
        except ValueError:
            return datetime.strptime(TIME, '%d-%m月 -%y %I.%M.%S.%f000 下午')
        # print(TIME,"is not a right format",sep=' ')

def time_fix_loop(TABLE):
    for i in range(len(TABLE)):
        TABLE.at[i,'UPDATETIME']=timetodt( TABLE.at[i, 'UPDATETIME'] )

time_fix_loop("TABLENAME") # eg. aqi_2014
```
<b> IMPORTANT: use `at` instead of `loc` or `iloc`. (`at` is 1000x faster than loc&iloc) </b>

* Or you can print message during converting to prevent speculating that your computer is not running
```python3
def time_fix_loop(TABLE):
    for i in range(len(TABLE)):
        print("Coverting number",i,sep=' ',end='...')
        TABLE.at[i,'UPDATETIME']=timetodt( TABLE.at[i, 'UPDATETIME'] )
        print("Done","(",len(TABLE)-i-1,"lefted",")",
             sep=' ')
```

* (experinmental) another way to convert time
```python3
def time_fix_loop_beta(TABLE):
    TABLE['UPDATETIME'] = TABLE['UPDATETIME'].apply(lambda a: timetodt(a))
```