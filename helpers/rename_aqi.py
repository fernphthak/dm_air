import os
import numpy as np

area_chinese=[u'中部空品區',u'北部空品區',u'宜蘭空品區',u'竹苗空品區',u'花東空品區',u'離島監測站',u'雲嘉南空品區',u'高屏空品區']
area_english=['central','north','yilan','zhu_miao','hua_dong','outlying','yun_jia_nan','gao_ping']

def rename_aqi(PATH,year):
        minguo=year-1911
        new_filename = ''
        for filename in os.listdir(PATH):
                if filename.startswith(str(minguo)+str(u'年 ')):
                        new_filename += str(year) + str('-')
                        new_filename += str(toEnglish(filename.replace(str(minguo)+str(u'年 '),'')))
                elif filename.startswith(str(minguo)+str(u'年')):
                        new_filename += str(year) + str('-')
                        new_filename += str(toEnglish(filename.replace(str(minguo)+str(u'年'),'')))
                print("rename",filename,"to", new_filename)
                target=os.path.join(".",PATH,filename)
                new_target=os.path.join(".",PATH,new_filename)
                os.rename(target, new_target)
                new_filename = ''

def toEnglish(WORD):
        for i in np.arange(0,len(area_chinese)):
                if WORD == area_chinese[i]:
                        return area_english[i]