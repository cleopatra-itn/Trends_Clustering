import pandas as pd
import sqlite3
import os
import datetime
import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as nsn

con = sqlite3.connect("DATABASE.db")
events = pd.read_sql_query("SELECT * from EVENT ", con)
concepts = pd.read_sql_query("SELECT * from CONCEPT ", con)
categories = pd.read_sql_query("SELECT * from CATEGORY ", con)

all1 = pd.merge(events, concepts, how='left', left_on='PID', right_on='FID')
all2 = pd.merge(events, categories, how='left', left_on='PID', right_on='FID')

gaurdianEc = all1[all1['SOURCE'] == "theguardian.com"]
gaurdianEca = all2[all2['SOURCE'] == "theguardian.com"]

wsjEc = all1[all1['SOURCE'] == "wsj.com"]
wsjEca = all2[all2['SOURCE'] == "wsj.com"]

nytEc = all1[all1['SOURCE'] == "nytimes.com"]
nytEca = all2[all2['SOURCE'] == "nytimes.com"]

wpEc = all1[all1['SOURCE'] == "washingtonpost.com"]
wpEca = all2[all2['SOURCE'] == "washingtonpost.com"]

cdEc = all1[all1['SOURCE'] == "chinadaily.com.cn"]
cdEca = all2[all2['SOURCE'] == "chinadaily.com.cn"]

tiEc = all1[all1['SOURCE'] == "timesofindia.indiatimes.com"]
tiEca = all2[all2['SOURCE'] == "timesofindia.indiatimes.com"]

smhEc = all1[all1['SOURCE'] == "smh.com.au"]
smhEca = all2[all2['SOURCE'] == "smh.com.au"]

shEc = all1[all1['SOURCE'] == "asahi.com"]
shEca = all2[all2['SOURCE'] == "asahi.com"]

dawnEc = all1[all1['SOURCE'] == "dawn.com"]
dawnEca = all2[all2['SOURCE'] == "dawn.com"]

zamanEc = all1[all1['SOURCE'] == "zaman.com.tr"]
zamanEca = all2[all2['SOURCE'] == "zaman.com.tr"]

# only valid index of categories
ind = []
for index, row in all2.iterrows():
    if type(all2.at[index, 'URI']) == float:
        ind.append(index)
all2.drop(ind,inplace=True)

# Total rare categories
g = Counter(" ".join(all2["URI"]).split()).most_common()
cou = 0
for a in range(len(g)):
    if g[a][1] < 2:
        cou += 1

# 100 frequent concepts
g = Counter(" ".join(all1["URI"]).split()).most_common(100)
test  = []
count  = 0
for a in range(len(g)):
    test.append(g[a][0])
    count += 1
    
#Only top 100 Wikipedia-Concepts   
all4 = all1[all1["URI"].isin(test)]

#Top 100 Wikipedia-Concepts for each newspaper   
gaurdianEc = all4[all4['SOURCE'] == "theguardian.com"]
wsjEc      = all4[all4['SOURCE'] == "wsj.com"]
nytEc      = all4[all4['SOURCE'] == "nytimes.com"]
wpEc       = all4[all4['SOURCE'] == "washingtonpost.com"]
cdEc       = all4[all4['SOURCE'] == "chinadaily.com.cn"]
tiEc       = all4[all4['SOURCE'] == "timesofindia.indiatimes.com"]
smhEc      = all4[all4['SOURCE'] == "smh.com.au"]
shEc       = all4[all4['SOURCE'] == "asahi.com"]
dawnEc     = all4[all4['SOURCE'] == "dawn.com"]
zamanEc    = all4[all4['SOURCE'] == "zaman.com.tr"]

#List for each newspaper
gaurdianEc_list = gaurdianEco["URI"].tolist()
wsjEc_list = wsjEco["URI"].tolist()
nytEc_list = nytEco["URI"].tolist()
wpEc_list = wpEco["URI"].tolist()
cdEc_list = cdEco["URI"].tolist()
tiEc_list = tiEco["URI"].tolist()
smhEc_list = smhEco["URI"].tolist()
shEc_list = shEco["URI"].tolist()
dawnEc_list = dawnEco["URI"].tolist()
zamanEc_list = zamanEco["URI"].tolist()

#matrix of values of all newspapers
ecval = [
    gaurdianEc_list,
    wsjEc_list,
    nytEc_list,
    wpEc_list,
    cdEc_list,
    tiEc_list,
    smhEc_list,
    shEc_list,
    dawnEc_list,
    zamanEc_list
]

# Trends for Top 100 Wikipedia-Concepts for each newspaper 
from statsmodels.tsa.filters.hp_filter import hpfilter
import plotly.express as px

gauPol = gaurdianEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")
wsPol = wsjEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")
nyPol = nytEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")
wPol = wpEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")
cPol = cdEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")
tPol = tiEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")
smPol = smhEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")
sPol = shEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")
dawPol = dawnEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")
zamaPol = zamanEc.groupby(["EVENTDATE", 'URI']).size().reset_index(name="count")

gauPol2 = gaurdianEc.groupby(['EVENTDATE', 'URI'])['URI'].count()
wsPol2 = wsjEc.groupby(['EVENTDATE', 'URI'])['URI'].count()
nyPol2 = nytEc.groupby(['EVENTDATE', 'URI'])['URI'].count()
wPol2 = wpEc.groupby(['EVENTDATE', 'URI'])['URI'].count()
cPol2 = cdEc.groupby(['EVENTDATE', 'URI'])['URI'].count()
tPol2 = tiEc.groupby(['EVENTDATE', 'URI'])['URI'].count()
smPol2 = smhEc.groupby(['EVENTDATE', 'URI'])['URI'].count()
sPvol2 = shEc.groupby(['EVENTDATE', 'URI'])['URI'].count()
dawPol2 = dawnEc.groupby(['EVENTDATE', 'URI'])['URI'].count()
zamaPol2 = zamanEc.groupby(['EVENTDATE', 'URI'])['URI'].count()

remaining1, trend1 = hpfilter(gauPol2, lamb=129600)
remaining1, trend2 = hpfilter(wsPol2, lamb=129600)
remaining1, trend3 = hpfilter(nyPol2, lamb=129600)
remaining1, trend4 = hpfilter(wPol2, lamb=129600)
remaining1, trend5 = hpfilter(cPol2, lamb=129600)
remaining1, trend6 = hpfilter(tPol2, lamb=129600)
remaining1, trend7 = hpfilter(smPol2, lamb=129600)
remaining1, trend8 = hpfilter(sPvol2, lamb=129600)
remaining1, trend9 = hpfilter(dawPol2, lamb=129600)
remaining1, trend10 = hpfilter(zamaPol2, lamb=129600)

trend1 = trend1.reset_index()
trend2 = trend2.reset_index()
trend3 = trend3.reset_index()
trend4 = trend4.reset_index()
trend5 = trend5.reset_index()
trend6 = trend6.reset_index()
trend7 = trend7.reset_index()
trend8 = trend8.reset_index()
trend9 = trend9.reset_index()
trend10 = trend10.reset_index()


# values for each newspaper
pcs = trend1['URI'].unique().tolist()


#Points for each trendline to be able to find DTW distance
val = []
for a in range(len(pcs)):
    x = []
    b = trend1[trend1['URI'] == pcs[a]]
    for index, row in b.iterrows():
        x.append([index, row['URI_trend']])
    val.append(x)

    
#DTW distance between each newspapers
from cdtw import pydtw
from dtaidistance import dtw
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cosine

mat = []
matrixA = {}
xv = []
maxS = 0

for a in range(len(val)):
    ro  =[]
    b = a+1
    print(a)
    while(b < len(val)):
        if b%900 == 0:
            print(b)
        d3,_=fastdtw(val[a], val[b], dist=cosine)        
        ro.append(str(round(d3,2)))
        if d3 < 0.1:
            xv.append(pcs[a] +" "+ pcs[b])
        b=b+1
        if d3 > maxS:
            maxS = d3
        
    #matrixA[ecs[a]] = ro
    #mat.append(ro)
    
print(len(xv))
ecval.append(xv)
print(maxS)

# Jaccard similarity for DTW and Eucliean distance
ecmatrix = []

for a in range(9):
    x = necval[a]
    nar = []
    for b in range(9):
        y = necval[b]
        nar.append(jaccard_similarity(x,y))
    ecmatrix.append(nar)