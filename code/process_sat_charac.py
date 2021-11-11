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
files = [f for f in files if f.endswith('.xls') and re.match(r'[A-Za-z]+\_[A-Za-z]+\_[A-Za-z]+\_\d+\.\w+', f)]
 
# files_sublist = ['sat_2017.csv', 'sat_2018.csv', 'sat_2019.csv']
files_sublist = files
dict_states = {}

#header_list_sat = ['Characteristics', 'Participation Rate', 'EBRW', 'Math', 'Total']
ls_sat_df = []
dict_charac_names = {
    'Associate degree' : "Associate's Degree", 
    "Associate's degree" : "Associate's Degree",  
    "Doctor's or related degree" : "Doctoral or related degree",
    'Doctoral or related degree' : 'Doctoral or related degree',
    '$10,000 to $20,000' : 'Less than $20,000', 
    'Less than $10,000' : 'Less than $20,000', 
    'Less than $20,000' : 'Less than $20,000', 
    '$10,000, but less than $20,000' : 'Less than $20,000',
    '$20,000, but less than $30,000' : '$20,000, to $40,000', 
    '$20,000, but less than $40,00' : '$20,000, to $40,000',
    '$20,000, but less than $40,000' : '$20,000, to $40,000', 
    '$30,000, but less than $40,000' : '$20,000, to $40,000',
    '$40,000, but less than $50,000' : '$40,000, to $60,000', 
    '$40,000, but less than $60,000' : '$40,000, to $60,000',
    '$50,000, but less than $60,000' : '$40,000, to $60,000', 
    '$60,000, but less than $70,000' : '$60,000, to $80,000',
    '$60,000, but less than $80,000' :  '$60,000, to $80,000', 
    '$70,000, but less than $80,000' :  '$60,000, to $80,000',
    '$80,000 to $100,000' : '$80,000 to $100,000', 
    '$80,000, but less than $100,000' :  '$80,000 to $100,000',
    '$100,000, but less than $120,000' : '$100,000, to $150,000',
    '$100,000, but less than $140,000' : '$100,000, to $150,000',
    '$120,000, but less than $140,000' : '$100,000, to $150,000',
    '$140,000, but less than $160,000' : '$100,000, to $150,000',
    '$140,000, but less than $200,000' : '$150,000, to $200,000',
    '$160,000, but less than $200,000' : '$150,000, to $200,000',
    'More than $100,000' : '$100,000, to $150,000',
    'A  (93-96)' : 'A (93-96)',
    'A (93-96)'  : 'A (93-96)',
    'B  (80-89)' : 'B (80-89)',
    'B (80-89)'  : 'B (80-89)',
    'C  (70-79)'  : 'C (70-79)',
    'C (70-79)'  : 'C (70-79)'
}

dict_charac_names_intended_major = {
 "Agriculture and related sciences"	:	"Agriculture and Related Sciences",
 "Agriculture, agriculture operations,\n     and related sciences"	:	"Agriculture and Related Sciences",
 "Agriculture, agriculture operations, and related \n     sciences"	:	"Agriculture and Related Sciences",
 "Agriculture, agriculture operations, and related sciences"	:	"Agriculture and Related Sciences",
 "Agriculture/natural resources"	:	"Agriculture and Related Sciences",
 "and related sciences"	:	"Agriculture and Related Sciences",
 "Architecture and related services"	:	"Architecture",
 "Architecture/environmental design"	:	"Architecture",
 "Area, ethnic, cultural, and gender\n     studies"	:	"Area, Ethnic, Cultural, and Gender Studies",
 "Area, ethnic, cultural, and gender studies"	:	"Area, Ethnic, Cultural, and Gender Studies",
 "studies"	:	"Area, Ethnic, Cultural, and Gender Studies",
 "Arts: visual/performing"	:	"Arts: Visual/Performing",
 "Biological and biomedical sciences"	:	"Biological and Biomedical Sciences",
 "Biological sciences"	:	"Biological and Biomedical Sciences",
 "Business and commerce"	:	"Business and Commerce",
 "Business management, marketing, and\n     related support services"	:	"Business and Commerce",
 "Business, management, marketing, and related support\n     services"	:	"Business and Commerce",
 "Business, management, marketing, and related support \n     services"	:	"Business and Commerce",
 "and related support services"	:	"Business and Commerce",
 "related support services"	:	"Business and Commerce",
 "Communication, journalism,\n     and related programs"	:	"Communications and Journalism",
 "Communication, journalism, and related programs"	:	"Communications and Journalism",
 "Communications"	:	"Communications and Journalism",
 "Communications and journalism"	:	"Communications and Journalism",
 "and related programs"	:	"Communications and journalism",
 "Computer and information sciences\n     and support services"	:	"Computer and Information sciences",
 "Computer and information sciences and support services"	:	"Computer and Information sciences",
 "Computer or information sciences"	:	"Computer and Information sciences",
 "and support services"	:	"Computer and Information sciences",
 "Construction trades"	:	"Construction Trades",
 "Construction trades, general"	:	"Construction Trades",
 "Education"	:	"Education",
 "Engineering"	:	"Engineering",
 "Engineering technologies/\n     technicians"	:	"Engineering Technologies",
 "Engineering technologies/technicians"	:	"Engineering Technologies",
 "Engineering technologies/techniques"	:	"Engineering Technologies",
 "technicians"	:	"Engineering Technologies",
 "English language and literature/\n     letters"	:	"English Language and Literature",
 "English language and literature/letters"	:	"English Language and Literature",
 "letters"	:	"English Language and Literature",
 "Family and consumer sciences/\n     human sciences"	:	"Family and Consumer Sciences",
 "Family and consumer sciences/human sciences"	:	"Family and Consumer Sciences",
 "human sciences"	:	"Family and Consumer Sciences",
 "Foreign languages and literatures, general"	:	"Foreign languages and literatures",
 "Foreign languages, literatures,\n     and linguistics"	:	"Foreign languages and literatures",
 "Foreign/classical languages"	:	"Foreign languages and literatures",
 "Foreign/classical languages "	:	"Foreign languages and literatures",
 "and linguistics"	:	"Foreign languages and literatures",
 "General/interdisciplinary"	:	"General/Interdisciplinary",
 "Health and allied services"	:	"Health And Allied Services",
 "Health professions and related\n     clinical services"	:	"Health And Allied Services",
 "Health professions and related clinical sciences"	:	"Health And Allied Services",
 "Health professions and related clinical services"	:	"Health And Allied Services",
 "clinical services"	:	"Health And Allied Services",
 "History"	:	"History",
 "History, general"	:	"History",
 "Home economics"	:	"Home Economics",
 "Language and literature"	:	"Language And Literature",
 "Legal professions and studies"	:	"Legal Professions And Studies",
 "Legal studies, general"	:	"Legal Professions And Studies",
 "Liberal arts and sciences, general\n     studies, and humanities"	:	"Liberal Arts And Sciences, General Studies, And Humanities",
 "Liberal arts and sciences, general studies, and \n     humanities"	:	"Liberal Arts And Sciences, General Studies, And Humanities",
 "Liberal arts and sciences, general studies, and humanities"	:	"Liberal Arts And Sciences, General Studies, And Humanities",
 "studies, and humanities"	:	"Liberal Arts And Sciences, General Studies, And Humanities",
 "Library and archival sciences"	:	"Library And Archival Sciences",
 "Library science and administration"	:	"Library Science And Administration",
 "Library science/librarianship"	:	"Library Science/Librarianship",
 "Mathematics"	:	"Mathematics",
 "Mathematics and statistics"	:	"Mathematics",
 "Mechanic and repair technologies/\n     technician"	:	"Mechanic And Repair Technologies Technician",
 "Mechanic and repair technologies/technicians"	:	"Mechanic And Repair Technologies Technician",
 "technician"	:	"Mechanic And Repair Technologies Technician",
 "Military sciences"	:	"Military Sciences",
 "Military technologies"	:	"Military Technologies",
 "Military technologies and applied\n     sciences"	:	"Military Technologies",
 "sciences"	:	"Military Technologies",
 "Multi/interdisciplinary studies"	:	"Multi/Interdisciplinary Studies",
 "Natural resources and conservation"	:	"Natural Resources And Conservation",
 "Other"	:	"Other",
 "Parks, recreation, and leisure studies"	:	"Parks, Recreation, And Leisure Studies",
 "Parks, recreation, leisure, and\n     fitness studies"	:	"Parks, Recreation, And Leisure Studies",
 "fitness studies"	:	"Parks, Recreation, And Leisure Studies",
 "Personal and culinary services"	:	"Personal And Culinary Services",
 "Personal and culinary services, general"	:	"Personal And Culinary Services",
 "Philosophy and religious studies"	:	"Philosophy And Religious Studies",
 "Philosophy/religion/theology"	:	"Philosophy And Religious Studies",
 "Philosophy/religious studies"	:	"Philosophy And Religious Studies",
 "Physical sciences"	:	"Physical Sciences",
 "Precision production"	:	"Precision Production",
 "Psychology"	:	"Psychology",
 "Psychology, general"	:	"Psychology",
 "Public administration and social\n     services"	:	"Public Administration And Social Services",
 "Public administration and social service professions"	:	"Public Administration And Social Services",
 "services"	:	"Public Administration And Social Services",
 "Public affairs and services"	:	"Public Affairs And Services",
 "Security and protective services"	:	"Security And Protective Services",
 "Social sciences"	:	"Social Sciences",
 "Social sciences and history"	:	"Social Sciences",
 "Technical and vocational"	:	"Technical And Vocational",
 "Theology and religious vocations"	:	"Theology And Religious Vocations",
 "Transportation and materials moving"	:	"Transportation And Materials Moving",
 "Undecided"	:	"Undecided",
 "Visual and performing arts, general"	:	"Visual And Performing Arts, General"
}

dict_sat_score_columns = {
    2000:[[0,7,8,9],['Characteristics','Reading','Math', 'Percentage Distribution']],
    2001:[[0,10,11,12],['Characteristics','Reading','Math', 'Percentage Distribution']],
    2002:[[0,10,11,12],['Characteristics','Reading','Math', 'Percentage Distribution']],
    2003:[[0,10,11],['Characteristics','Reading','Math']],
    2004:[[0,11,12,13],['Characteristics','Reading','Math', 'Percentage Distribution']],
    2005:[[0,14,15],['Characteristics','Reading','Math']],
    2006:[[0,14,15,16,17],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2007:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2008:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2009:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2010:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2011:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2012:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2013:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2014:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2015:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2016:[[0,15,16,17,18],['Characteristics','Reading','Math','Writing', 'Percentage Distribution']],
    2017:[[0,4,5,2],['Characteristics','Reading','Math', 'Percentage Distribution']],
    2018:[[0,9,10,7],['Characteristics','Reading','Math', 'Percentage Distribution']],
    2019:[[0,14,15,12],['Characteristics','Reading','Math', 'Percentage Distribution']]

}

ls_category = ['All students',
'High school rank',
'High school grade point average',
'Intended college major',
'Degree-level goal',
'Highest level of parental education',
'High school type',
'Family income']


def clean_state_names(x):
    #return re.search('^\s*([a-zA-Z]+\s*?[a-zA-Z]+\s*?[a-zA-Z]+).*$', x).group(1)
    x = x.replace('.','')
    x = re.sub('\\\\\d\\\\', '',x)
    return x.strip()

for file in files_sublist:
    
    df = pd.read_excel(os.path.join(inputfilespath, file), header = None, na_values = [r'(\2\)', r'#', r'---', r'â€'])
    #df = pd.read_excel(os.path.join(inputfilespath, file), header = None) 
    

    #Reading only the rows between United States and Wisconsin
    start_row = df[df.iloc[:,0].str.contains('All students', case=False, na=False)].index[0]
    end_row = df[df.iloc[:,0].str.contains('Graduate Degree|Undecided', case=False, na=False)].index[-1]
    #print(df.iloc[start_row:,0].str.contains('_', case=False, na=False))
    df = df.iloc[start_row:end_row+1,:]
    #print(df.head())
    #Dropping NaN rows from states columns. Blank rows in the input excel file had NaN values in dataframe
    df.dropna(subset = [df.columns[0]], inplace = True)

    #Removing spaces and '....' characters from state names
    df.iloc[:,0] = df.iloc[:,0].apply(clean_state_names)

    #Removing columns with | which was present as a delimiter in the excel file
    df = df.loc[:, ~(df == '|').any()]

    #Dropping any erroneous rows and columns which were all NaN
    df.dropna(axis=1, thresh = 30, inplace=True)
    #df.dropna(axis=0, thresh = 4, inplace=True)

    #Replacing Columbia with District of Columbia
    #df.iloc[:,0].replace(regex=r'^Columbia',value='District of Columbia', inplace=True)

    #Renaming column names to make it consistent range
    df.columns = np.arange(len(df.columns))

    #Extracting the year from the file name. file name format = sat_2009.xls
    year = re.findall(r'\d+', file)[0]
    year = int(year)
    df = df[dict_sat_score_columns[year][0]]
    df.columns = dict_sat_score_columns[year][1]
    df['Year'] = year

    #attempting to identify category
    #df['Category'] = np.nan
    df['Category'] = df['Characteristics'].apply(lambda x: x if x in ls_category else np.nan )
    df['Category'].fillna(method='ffill',inplace=True)
    df.dropna(axis=0,  thresh = 4, inplace=True)
    #df = df.apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in str(x)]))
    #print(f' {df.shape} {year} ' )
    ls_sat_df.append(df)
    #print (f'{file} {df.shape(0)}')
    #dict_states[file] = list(df['Characteristics'])
    #print (df.head(3))
df = pd.concat(ls_sat_df, ignore_index=True)
df = df[['Characteristics', 'Category', 'Year', 'Reading', 'Math', 'Writing', 'Percentage Distribution']]
#print (df.head(3))

#These two steps are repetitive. These were required as the applymap function was behaving weirdly. NaN was getting
#replaced to nan as a string and dates were becoming integer garbage
df = df.replace(np.nan, 0)
#df['Year'] = pd.to_datetime(df['Year'], format='%Y')

#to remove â€ character which was in input excel
df = df.applymap(lambda x: ''.join(["" if (ord(i) < 32 or ord(i)) > 126 else i for i in str(x)]))

#replacing blank cells with nan
#df = df.replace(np.nan, 0)
df = df.apply(pd.to_numeric, errors='ignore')
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

df['Characteristics'] = df['Characteristics'].apply(lambda x : dict_charac_names[x] if x in dict_charac_names else x)
df['Characteristics'] = df['Characteristics'].apply(lambda x : dict_charac_names_intended_major[x] if x in dict_charac_names_intended_major else x)
#print(df['Characteristics'].unique())
#print(df.info())
#for jupyter notebook
df.to_csv('../exported_data/sat_characteristics_2000_2019.csv')
""" #for python script
df.to_csv('./exported_data/sat_characteristics_2000_2019.csv') """

