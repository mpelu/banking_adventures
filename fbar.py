import pandas as pd

class AccountDF:

    def __init__(self, name, file_name):
        self.name = name + ' Account'
        self.file_name = file_name
        self.df = pd.read_csv(file_name) # DataFrame object

    # basic functions

    def head(self):
        print(self.df.head())

    def file_metadata(self):
        print(self.df.info())       

    # TODO check for more elegant solution
    def transaction_breakdown(self):
        truncated_df = self.df.iloc[:, [2, 3, 4]]
        truncated_df.columns = ['Withdrawals', 
                                'Deposits', 
                                'Total Transactions']
        row_count = truncated_df.count() # Series object
        print(row_count)


    # fbar functions

    def max_balance(self):
        print('Highest balance of', self.name , ': ' , self.df['Balance'].max()) 

    def total_income(self):
        filtered_df = self.df[self.df['Transaction_Desc'].str.contains("INTEREST CREDIT")]
        total_income = filtered_df['Deposits'].sum()
        print(total_income)

        
ch = AccountDF('Checking', 'checking.csv')
ch.max_balance()
ch.file_metadata()

sa = AccountDF('Savings', 'savings.csv')
sa.max_balance()
sa.file_metadata()
sa.total_income()
sa.head()
sa.transaction_breakdown()


