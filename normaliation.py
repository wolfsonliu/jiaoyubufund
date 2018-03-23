# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:46:33 2018

@author: lib
"""
import os
import pandas as pd
dir_pdf = './pdf'
dir_txt = './txt'
dir_csv = './csv'

with open(os.path.join(dir_txt, 'W020160608577758511773.txt'), 'rb') as file:
    with open(os.path.join('./', 'W020160608577758511773_good.txt'), 'wb') as good:
        with open(os.path.join('./', 'W020160608577758511773_bad.txt'), 'wb') as bad:
            for x in file:
                y = x.decode('utf-8')
                if y == '\n':
                    continue
                elif y[0] in str(list(range(10))) and len([z for z in y.split(' ') if z]) == 6:
                    good.write(','.join([z for z in y.split(' ') if z]).encode('utf-8'))
                else:
                    bad.write(y.encode('utf-8'))

gooddata = pd.read_csv(os.path.join('./', 'W020160608577758511773_good.txt'), header=0)
gooddata.sort_values('序号', inplace=True)
gooddata['年份'] = 2016

gooddata[
    ['序号','学科门类','学校名称','项目类别','项目名称','申请人','年份']
].to_csv(os.path.join(dir_csv, 'W020160608577758511773.csv'), index=False, encoding='utf-8')