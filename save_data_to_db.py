
##insert data in sqlite database


import sklearn
import pandas as pd
from ast import literal_eval
import sqlite3
import csv


# TODO: db 직접 생성해보
# #db 생성
# con = sqlite3.connect('food_restaurants.db')
# sqlite3.Connection
#


# 기존에 생성해둔 db를 연다.
con = sqlite3.connect('db.sqlite3')



# csv 파일 읽기
df = pd.read_csv('korean_res.csv', engine = 'python', encoding = 'euc-kr')
#print(df)



#컬럼명 변경
df.columns = ["title" , 'cate1', 'cate2', 'cate3', 'local', 'city' , 'details']


#빈 셀은 제거
##drop all rows that have any NaN values
df = df.dropna()


# save sqlite db
# """
# if_exists : {'fail', 'replace', 'append'}, default 'fail'
#     - fail: If table exists, do nothing.
#     - replace: If table exists, drop it, recreate it, and insert data.
#     - append: If table exists, insert data. Create if does not exist.
# """
df.to_sql('test_app_restaurants',con , if_exists = 'append', index=False)

#df.to_sql('test_app_restaurants',con, if_exists = 'replace', index=False )
