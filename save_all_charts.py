#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:03:19 2018

@author: chengyu
"""
import pandas as pd 
#%matplotlib inline
## set up all plotly dependecies 
import matplotlib as mpl
import matplotlib.pyplot as plt
#import seaborn as sns
mpl.style.use('ggplot')
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

#%%
data_path = "data/results.xlsx"
df = pd.read_excel(data_path)
#%%

def save_chart(df,chart_title,savefilename,x='year_final',y=['sentindex'],xlabel='year',ylabel='Sentiment',size=(15,6)):
    '''
    x: string : time variable
    y: string : index variable, it can be a list as well
    '''
    fig = plt.figure(figsize=size)
    #ax = plt.axes()
    x = df[x]
    y = df[y]
    plt.plot(x,y)
    plt.title(chart_title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(savefilename)
    plt.close(fig)
    
#%%

countries = df[['country_code','imf_country_name']].copy()
countries.drop_duplicates('country_code',inplace=True)
countries.dropna(inplace=True)

for c in countries.imf_country_name.values:
    print(c)
    data = df[df['imf_country_name'] == c]
    save_chart(data,c,'charts/'+c+'.png')