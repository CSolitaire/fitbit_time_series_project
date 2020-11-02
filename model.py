import numpy as np
import pandas as pd

from datetime import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt

import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

import statsmodels.api as sm
from statsmodels.tsa.api import Holt

import warnings
warnings.filterwarnings("ignore")


##################################### Model Functions ########################################
def plot_and_eval(train, validate, yhat_df, target_var):
    "This function plots your RMSE on Train and Validate"
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var], label='Train', linewidth=1)
    plt.plot(validate[target_var], label='Validate', linewidth=1)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = round(sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 0)
    print(target_var, '-- RMSE: {:.0f}'.format(rmse))
    plt.show()

##############################################################################################


##############################################################################################


##############################################################################################
