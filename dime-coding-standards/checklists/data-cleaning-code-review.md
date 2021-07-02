# Data cleaning code review checklist

**Data source/survey round:**

**Date: 7/2/2021**  

## List of files to be checked
- Master script - runfile.do
- Clean dataset(s)- mw_trauma_analysis.dta/ tr_mwnopii_clean.dta
- Cleaning scripts - 1_cleaning.do

## Reproducibility
- [X] All scripts run from the master after adding the correct folder path to line(s) 32-33 
- [X] The master script is organized in a way that allows you to understand the general tasks being performed in the code
- [X] The master script tracks which scripts create and use which files
- [X] The datasets created by the reviewer are exactly the same as those shared by the coder

## Code organization and readability
- [X] Code file names are informative 
- [X] It is clear in the code why tasks are being executed
- [X] The code structure facilitates understanding of the tasks
- [X] Code uses white space to improve readability
- [X] There is extensive use of comments to explain the code
- [ ] The code is efficient (tasks are executed in the simplest way possible, loops are used when needed rather than repeating lines, pre-defined functions are used)
- [ ] Common tasks are abstracted and automated (e.g. using functions or macros)

## Clean dataset checks (pre-publication)
- [X] The data does not include direct identifiers
- [X] The dataset has a clearly labeled, uniquely and fully identifying ID variable(s)
- [X] The level of observation of the dataset is clear from the dataset name, ID variables, and documentation
- [X] Variables have informative labels or an accompanying dictionary
- [X] Categorical variables have clear and informative value labels
- [X] No modification is made from the raw to the clean data other than correcting problems 
- [ ] No raw variables are processed (winsorized, for example)  
- [X] Variables can be easily traced back to the original questionnaire
- [ ] Variables are sensibly ordered and dataset is compressed and saved in appropriate format

## Data cleaning tasks
- [X] Are new variables being created in the cleaning do-files? 
- [X] Are any changes being made to observations values in the cleaning do-files? 
- [ ] Check merges: Are any observations dropped? If so, is there a clear justification for that? If any observations didn't match, is that explained in the comments?
- [X] Are missing values coded consistently? Are extended missing values used?
