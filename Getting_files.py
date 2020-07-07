import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from bs4 import BeautifulSoup
import requests

df= pd.read_excel('cik_list.xlsx')

urls=[]
for i in df.index:
    url=df['SECFNAME'][i]
    urls.append(url)

cnt = 1
for url in urls:
    response = requests.get(url)
    file = BeautifulSoup(response.text, "html.parser")
    file2write = open("sec_{}.txt".format(cnt), "w+", encoding="UTF-8")
    cnt += 1
    file2write.write(file.text)
    file2write.close()

