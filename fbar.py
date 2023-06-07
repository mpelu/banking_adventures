import pandas as pd

class AccountDF:

    def __init__(self, name, file_name):
        self.name = name + ' Account'
        self.file_name = file_name
        self.data_frame = pd.read_csv(file_name) 


    # basic functions

    def head(self):
        print(self.data_frame.head())

    def file_metadata(self):
        print(self.data_frame.info())

  
    # fbar functions

    # TODO:
    # specify date range
    # add currency sign
    def max_balance(self):
        print('Highest balance of', self.name , ': ' , self.data_frame['Balance'].max()) 

    # TODO:
    # str.contains regex
    # add currency sign
    def sum_income(self):
        df = self.data_frame
        filtered_df = df[df['Transaction_Desc'].str.contains("INTEREST CREDIT")]
        total_income = filtered_df['Deposits'].sum()
        print(total_income)

ch = AccountDF('Checking', 'checking.csv')
ch.max_balance()
ch.file_metadata()

sa = AccountDF('Savings', 'savings.csv')
sa.max_balance()
sa.file_metadata()
sa.sum_income()
