# here we create data(data preparation)

import pandas as pd
import numpy as np


loan_data_backup = pd.read_csv('E:\programming\Data science\Credit risk modelling\support files\Loan data 2015\loan_data_2015.csv')

loan_data =loan_data_backup.copy()

#pd.options.display.max_columns = None

#it gives columns names
#loan_data.columns.values()

#it gives values types of columns
#loan_data.info()
print(loan_data.head())

'''
here we want to manipulate data type term and emp_length to float
as it in object type 
object in csv is string
'''

loan_data['emp_length_int'] = loan_data['emp_length'].str.replace('+ years','')
loan_data['emp_length_int'] = loan_data['emp_length_int'].str.replace('< 1 year', str(0))
loan_data['emp_length_int'] = loan_data['emp_length_int'].str.replace('n/a', str(0))
loan_data['emp_length_int'] = loan_data['emp_length_int'].str.replace(' years', '')
loan_data['emp_length_int'] = loan_data['emp_length_int'].str.replace(' year','')

print(loan_data['emp_length_int'].unique())

'''
but emp_length_int will str data type we need to transform it into float
'''

loan_data['emp_length_int'] = pd.to_numeric(loan_data['emp_length_int'])


'''
same process above we have to do for term'''


loan_data['term_int'] = loan_data['term'].str.replace(' months', '')
loan_data['term_int'] = loan_data['term_int'].str.replace(' ', '')
print('/n')
print(loan_data['term_int'].unique())


loan_data['term_int'] = pd.to_numeric(loan_data['term_int'])

loan_data['earliest_cr_line_date'] = pd.to_datetime(loan_data['earliest_cr_line'], format= '%b-%y')

print(pd.to_datetime('2017-12-01') - loan_data['earliest_cr_line_date'])

loan_data['months_since_earliest_cr_line'] = round(pd.to_numeric((pd.to_datetime('2017-12-01')- loan_data['earliest_cr_line_date'])/np.timedelta64(1,'M')))

print(loan_data['months_since_earliest_cr_line'].describe())
#loan_data.info()

#df.loc()
print(loan_data.loc[:,['earliest_cr_line', 'earliest_cr_line_date','months_since_earliest_cr_line']][loan_data['months_since_earliest_cr_line']<0])

loan_data['months_since_earliest_cr_line'][loan_data['months_since_earliest_cr_line']<0]-loan_data['months_since_earliest_cr_line'].max()

print(min(loan_data['months_since_earliest_cr_line']))