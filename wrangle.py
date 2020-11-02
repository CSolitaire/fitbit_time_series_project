
########################## Imports ##########################
import numpy as np
import pandas as pd
from datetime import datetime

########################## Wrangle Functions ##########################
def wrangle_fitbit_explore():
    "This function reads in a csv, converts date to datetime, sorts that index, and adds 3 categorical colums for explore"
    df = pd.read_csv('time_series_project.csv')
    df.date = pd.to_datetime(df.date)
    df = df.set_index('date').sort_index()
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['weekday'] = df.index.day_name()
    df = (df.astype({'Year': 'category', 
                'Month': 'category', 
                'weekday': 'category'}))
    return df

##############################################################################
def wrangle_fitbit_model():
    "This This function reads in a csv, converts date to datetime, and sorts that index"
    df = pd.read_csv('time_series_project.csv')
    df.date = pd.to_datetime(df.date)
    df = df.set_index('date').sort_index()
    return df