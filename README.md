# Loss Severity Modeling of Single-Family Residential Mortgage Loans
My team and I were working on a linear regression model to predict loss given default based on the variables that were meaningful to make the relevant prediction. Besides the variables that were found on the Fannie Mae mortgage loan dataset, macroeconomic variables like unemployment rate, FHA rate, and market to market loan to value ratio were also considered to be used in the model as well.

## Notice
- This repository was created by Hongyi Xia to present on the finalized code work for the sake of clarity and conciseness. Any intermediate working proceduce carried out by Hongyi Xia and his team members can be found at a different private repository.

- The actual raw dataset is absent in the repository given its bulk size

## Key files to highlight
 - MacroEconomicToMerge : The folder where all the wrangled macroeconomic variables are stored; there is also a python file that contain some dictionaries to transform relevant variable values

 - MacroEconomicVariables : The folder that stores the raw macroeconomic variables dataset prior to data wrangling

 - Data_cleaning.py : The Python file than can be applied on the Fannie Mae mortgage loan dataset zip file and stores it as csv file 

 - Data_modelling-testing.ipynb : The Python notebook that produces the draft 1 of the data wrangling and the draft 1 of the forward selection method 

 - Forward Selection.ipynb : The Python notebook that produces the draft 2 of the data wrangling and the final version of the forward selection method with stratified sampling 

 - Macro economic variable - Hongyi.ipynb : The Python notebook that produces the data wrangling of macroeconomic variables like unemployment rate, FHA rate, and State HPI, which will later be integrated with Fannie Mae mortgage loan dataset 

 - Model_A2.ipynb - The Python notebook that produces the final version of the overall data wrangling and some attempts to apply OLS model

 - base.csv : An empty dataframe with all the variables present (it is redundant in the final version of the data wrangling

 - exploratory_Analysis.ipynb : The Python notebook that provides the exploratory data analysis of mortgage loan datasets after applying the final version of the data wrangling

## Sampling and removing outlier
 - After finishing data wrangling, stratified sampling is appplied to make sure there are equal number of samples randomly choosen from various datasets of respective years and quarters

 - Based on the histogram of our predicting variable - Loss Given Default, there exist extreme outliers. A specific range of value of Loss Given Default is determined to retain the dominant distribution of Loss Given Default, where vast majority of the dataset observations are congregated. The figure below shows the histogram of Loss Given Default before and after removing outlier

![App Screenshot](../ImageREADME/outlier.png)

