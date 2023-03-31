# import pandas as pd

# # build my class of type dataframe
# # df is a dataframe object - objects are stored to variables.
# # when i create a new obj and save it to a variable,
# # i say that i have instantiated that object, meaning 
# # i've created one example of that object when that code is run
# # oop = object oriented programming - we can take a bundle of variables
# # and store them into a single name (object)
# df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

# if __name__ == '__main__':

#     # variables that form part of an object are called attributes
#     # we access variables called 'dot-notation' - example 'df.shape,' 
#     # or df.dtypes, df.columns, df.index
#     # print(df.shape)
#     # print(df.dtypes)
#     # print(df.index)
#     # print(df.columns)

#     # functions that form part of an 'obj' are called methods
#     print(df.head())
#     print(df.describe())
#     print(df.isnull().sum())

#     # method associated w/a pandas series object
#     # aka column of df
#     # that lives inside of a dataframe
#     print(df['a'].value_counts())

# ========================================

class Wallet:
    
    # first thing to run when making a new class
    # outline user provided input values here
    # parameters with default values assigned are optional
    def __init__(self, initial_amount = 0):
        # save user-provided initial amount as an attribute
        # self refers to whatever obj i'm working with
        self.balance = initial_amount
    
    # spend cash METHOD
    def spend_cash(self, amount):
        if self.balance < amount:
            return 'not enough shmeckles'
        else:
            self.balance = self.balance - amount
            return f'remaining balance: ${self.balance}'
        
    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f'new balance of: ${self.balance}'

    #__repr__ method
    # changes how the obj looks when it is printed out
    # the presence of the self keyword allows me to access or
    # modify class attributes within this function
    def __repr__(self):
        return f'Wallet with balance of: ${self.balance}'

if __name__ == '__main__':
    wallet1 = Wallet(100)
    wallet2 = Wallet(50)
    wallet3 = Wallet(3000)

    print(wallet1)
    print(wallet2)
    print(wallet3)