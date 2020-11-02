############################## Imports ##############################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
############################## Explore Functions ############################## 
def split_validate(df):
    "This function  splits df in to train, validate, test, and verify's the splits were done correctly (Time Series)"
    train_size = int(len(df)*.5)
    validate_size = int(len(df)*.3)
    test_size = int(len(df) - train_size - validate_size)
    validate_end_index = train_size + validate_size
    train = df[:train_size]
    validate = df[train_size:validate_end_index]
    test = df[validate_end_index:]
    
    print('Does the length of each df equate to the length of the original df?')
    print(len(train) + len(validate) + len(test) == len(df))
    
    print('Does the first row of original df equate to the first row of train?')
    print(df.head(1) == train.head(1))
    
    print('Is the last row of train the day before the first row of validate? And the same for validate to test?')
    pd.concat([train.tail(1), validate.head(1)])
    pd.concat([validate.tail(1), test.head(1)])
    
    print('Is the last row of test the same as the last row of our original dataframe?')
    pd.concat([test.tail(1), df.tail(1)])

    return train, validate, test

########################################################################################### 
def visualize_splits(train, validate, test):
    "This function visualizes numeric data in the train df"
    train = train.select_dtypes(include=np.number)
    validate = validate.select_dtypes(include=np.number)
    test = test.select_dtypes(include=np.number)
    for col in train.columns:
        plt.figure(figsize=(12,4))
        plt.plot(train[col])
        plt.plot(validate[col])
        plt.plot(test[col])
        plt.ylabel(col)
        plt.title(col)
        plt.show()


########################################################################################### 
def numeric_hists(df, bins=20):
    """
    Function to take in a DataFrame, bins default 20,
    select only numeric dtypes, and
    display histograms for each numeric column
    """
    plt.rc('figure', figsize=(11, 9))
    plt.rc('font', size=13)
    num_df = df.select_dtypes(include=np.number)
    num_df.hist(bins=bins, color='blue', ec='black')
    plt.suptitle('Numeric Column Distributions')
    plt.tight_layout()
    plt.show()

