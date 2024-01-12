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
 - After finishing data wrangling, stratified sampling was appplied to make sure there were equal number of samples randomly choosen from various datasets of respective years and quarters

 - Based on the histogram of our predicting variable - Loss Given Default, there existed extreme outliers. A specific range of value of Loss Given Default was determined to retain the dominant distribution of Loss Given Default, where vast majority of the dataset observations were congregated. The figure below shows the histogram of Loss Given Default before and after removing outlier

![image](./docs/outlier.png)

## Forward selection
- By performing forward selection with R-square as the weighting criteria, it was preferably to have a model with 10-12 factors based on the elbow method in the figure below. For a model with 12 factors, an adjusted R-square of about 0.324 was obtained.

![image](./docs/LGD_R2.png)

## Model validation
- The testing dataset was applied on the 12-factors model to validate how accurate the predicted Loss Given Default was compared to the actual Loss Given Default. Using an important variable market to market loan to value ratio (MTM-LTV) as an indicator for comparison, it could be realized in the figure created by Tableau below that the predicted average Loss Given Default was very close to the actual average Loss Given Default as long as there was a large enough sample size.

![image](./docs/LGD_dual_axis.png)
