import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re
import string
# import openpyxl
data_folder = 'downloaded_data'

#This part is needed for jupyter notebook
parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
inputfilespath = os.path.join(parentDirectory, data_folder)

""" #This part is needed for python script
inputfilespath = os.path.join(os.getcwd(), data_folder) """

files = os.listdir(inputfilespath)
# files = [f for f in files if f.endswith('.xls')]
files = [f for f in files if f.endswith('.xls') and re.match(r'[A-Za-z]+\_?\d+\.\w+', f)]
 
# files_sublist = ['sat_2017.csv', 'sat_2018.csv', 'sat_2019.csv']
files_sublist = files
dict_states = {}

#header_list_sat = ['State', 'Participation Rate', 'EBRW', 'Math', 'Total']
ls_sat_df = []

dict_sat_score_columns = {
    2000:[[0,11,12,14],['State','Reading','Math', 'Percent of Graduates taking SAT']],
    2001:[[0,11,12,14],['State','Reading','Math', 'Percent of Graduates taking SAT']],
    2002:[[0,11,12,14],['State','Reading','Math', 'Percent of Graduates taking SAT']],
    2003:[[0,11,12,14],['State','Reading','Math', 'Percent of Graduates taking SAT']],
    2004:[[0,11,12,14],['State','Reading','Math', 'Percent of Graduates taking SAT']],
    2005:[[0,13,14,16],['State','Reading','Math', 'Percent of Graduates taking SAT']],
    2006:[[0,11,12,13,15],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2007:[[0,12,13,14,16],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2008:[[0,13,14,15,17],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2009:[[0,13,14,15,17],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2010:[[0,14,15,16,18],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2011:[[0,14,15,16,18],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2012:[[0,14,15,16,18],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2013:[[0,14,15,16,18],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2014:[[0,14,15,16,18],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2015:[[0,14,15,16,18],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2016:[[0,14,15,16,18],['State','Reading','Math','Writing', 'Percent of Graduates taking SAT']],
    2017:[[0,3,5,13],['State','Reading','Math', 'Percent of Graduates taking SAT']],
    2018:[[0,10,12,14],['State','Reading','Math', 'Percent of Graduates taking SAT']],
    2019:[[0,17,19,21],['State','Reading','Math', 'Percent of Graduates taking SAT']]

}

def clean_state_names(x):
    return re.search('^^\s*([a-zA-Z]+\s*?[a-zA-Z]+\s*?[a-zA-Z]+).*$', x).group(1)

for file in files_sublist:
    
    df = pd.read_excel(os.path.join(inputfilespath, file), header = None) 

    #Reading only the rows between United States and Wisconsin
    start_row = df[df.iloc[:,0].str.contains('United States', case=False, na=False)].index[0]
    end_row = df[df.iloc[:,0].str.contains('Wyoming', case=False, na=False)].index[0]
    df = df.iloc[start_row:end_row+1,:]

    #Dropping NaN rows from states columns. Blank rows in the input excel file had NaN values in dataframe
    df.dropna(subset = [df.columns[0]], inplace = True)

    #Removing spaces and '....' characters from state names
    df.iloc[:,0] = df.iloc[:,0].apply(clean_state_names)

    #Removing columns with | which was present as a delimiter in the excel file
    df = df.loc[:, ~(df == '|').any()]

    #Dropping any erroneous rows and columns which were all NaN
    df.dropna(axis=1, thresh = 30, inplace=True)
    df.dropna(axis=0, thresh = 10, inplace=True)

    #Replacing Columbia with District of Columbia
    df.iloc[:,0].replace(regex=r'^Columbia',value='District of Columbia', inplace=True)

    #Renaming column names to make it consistent range
    df.columns = np.arange(len(df.columns))

    #Extracting the year from the file name. file name format = sat_2009.xls
    year = re.findall(r'\d+', file)[0]
    year = int(year)
    df = df[dict_sat_score_columns[year][0]]
    df.columns = dict_sat_score_columns[year][1]
    df['Year'] = year

    #print(df.iloc[:3,:])
    #print(f' {df.shape} {year} ' )
    ls_sat_df.append(df)
    #print (f'{file} {df.shape(0)}')
    #dict_states[file] = list(df['State'])
    #print (df.head(3))
df = pd.concat(ls_sat_df, ignore_index=True)
df = df[['State', 'Year', 'Reading', 'Math', 'Writing', 'Percent of Graduates taking SAT']]
df = df.apply(pd.to_numeric, errors='ignore')
df['Year'] = pd.to_datetime(df['Year'], format="%Y")
#print(df.info())
#for jupyter notebook
df.to_csv('../exported_data/sat_scores_2000_2019.csv')
""" #for python script
df.to_csv('./exported_data/sat_scores_2000_2019.csv') """

