# Fitbit Time Series Project

### Author: Corey Solitaire

## Project Goals: 
To review six months of Fitbit data in order to characterize the person who wore the fitness tracker (employee or test subject status unknown) and predict the next two weeks worth of data that is missing.  

## Deliverables:
1. A jupyter notebook containing your analysis
2. A clean data set. The source data is a little messy and there is some work that needs to be done before you can effectively work with it. Your notebook should include the code to go from the original source data to a data set that you can work with.
3. A summarization of the data, ie what can you say about the individual who was wearing this fitness tracker?
4. Predictions for the missing two weeks worth of data in a separate csv file.


## Executive Summary: 

**Project Summary:**   
The purpose to this project was to clean and explore an unlabled fitness tracker dataset, to provide evidence to support characterization of an individual, and to utilize time series analysis to predict two missing weeks of tracker data.  

**Background:**   
Here at Big Research Co.®, we love data so much - everyone wears Fitbits, even our employees! We believe these watches are the next step in the Big Data Industry and help enhance our current research. Our research spans from fitness equipment and drug trials to very ethical human experimentation. However, someone in a research and develoment lab mixed up the labels for our Fitbit datasets and one was left out.

**Process:**   
Data set was combined from eight csv files in Excel. 97% of food log data was missing, so values were dropped. This resulted in a data frame that was 10 columns by 225 rows, with each row representing a specific day. Data was explored and weekly trends were obsereved. Data was applied to several time series models, with a seven-day moving average providing the lowest RMSE. When this model was applied, it resulted in a 29% improvement over baseline (last observed value).  

**Results and Conclusions:**   
General trends in the data demonstrate a slight upward trend in calories and activity over time, with the majority of higher activity levels occuring on the weekend. The lack of regular exercise, the lenght of time spendt sedentary and the the missing food data suggest this fitness tracker belongs to an employee. While the model was able to improve on baseline observations, I was not able to match a model to weekly seasonality. There exists the possibility that alternate modeling techiniques (TSA with Prophet) would return better results; however, this modeling technique was not included in this study. 

**Reccomendations:**   
- **Not Enough Data:** With only seven months of data, it was difficult to pick up longterm trends in seasonality. More data would have yeilded better results. 
- **New Model:** Spending time refining previous cycle model and exploring Prophet would improve model forcasting.   
- **Cross Validation:**  Time-based splitting can provide statistically robust model evaluation and best simulate real-life scenarios. Exploring the use of time-based cross validation to form a type of “sliding window” average would most likely lead to better model results.  

## Instructions for Replication:
Files are located in Git Repo [here](https://github.com/CSolitaire/fitbit_time_series_project)
User will need env.py file with access to Codeup database 


## Data Dictionary:
| Column Name         | Description                                               |
|---------------------|-----------------------------------------------------------|
| date                | yyyy-mm-dd, df index                                      |
| cals_burned         | calories burned for the day                               |
| steps               | steps taken in the day                                    |
| dist                | distance walked, possibly in miles                        |
| floors              | uncertain, possible floors walked up or down              |
| mins_sedentary      | minutes of the day sedentary                              |
| mins_lightly_active | minutes of the day lightly active                         |
| mins_fairly_active  | minutes of the day fairly active                          |
| mins_very_active    | minutes of the day vary active                            |
| activity_cals       | uncertain, possibly calories burned due to active minutes |
| month               | month of the observation                                  |
| weekday             | weekday of the observation                                |  

## Audience:
- Data Science Team 

## Setting:
- Professional

## Workflow:
![](https://github.com/CSolitaire/zillow_cluster_project/blob/main/pipeline%20copy.jpg)