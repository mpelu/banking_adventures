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


ch = AccountDF('Checking', 'checking.csv')
ch.max_balance()
ch.file_metadata()

sa = AccountDF('Savings', 'savings.csv')
sa.max_balance()
sa.file_metadata()
