import os
import numpy as np

area_chinese={u'中部空品區',u'北部空品區',u'宜蘭空品區',u'竹苗空品區',u'花東空品區',u'離島監測站',u'雲嘉南空品區',u'高屏空品區'}
area_english={'central','north','yilan','zhu_miao','hua_dong','outlying','yun_jia_nan','gao_ping'}

def rename_aqi(PATH,year):
        minguo=year-1911
        for filename in os.listdir(PATH):
                if filename.startswith(minguo+u'年'):
                        os.rename(filename, year+'-'
                                +toEnglish(filename.replace(minguo+u'年','')))
                elif filename.startswith(minguo+u' 年 '):
                        os.rename(filename, year+'-'
                                +toEnglish(filename.replace(minguo+u'年 ','')))

def toEnglish(WORD):
        for i in np.arange(0,len(area_chinese)):
                if WORD == area_chinese[i]:
                        return area_english[i]