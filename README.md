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
def time_fix_loop(TABLE):
    for i in range(len(TABLE)):
        TABLE.loc[i,'UPDATETIME']=rd.timetodt( TABLE.loc[i, 'UPDATETIME'] )

time_fix_loop("TABLENAME") # eg. aqi_2014
```