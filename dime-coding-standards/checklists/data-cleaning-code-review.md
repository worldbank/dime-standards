# Data cleaning code review checklist

**Data source/survey round:**

**Date:**  

## List of files to be checked [Add names or links]
- Master script
- Clean dataset(s)
- Cleaning scripts

## Reproducibility
- [ ] All scripts run from the master after adding the correct folder path to line(s) X (and XX)
- [ ] The master script is organized in a way that allows you to understand the general tasks being performed in the code
- [ ] The master script tracks which scripts create and use which files
- [ ] The datasets created by the reviewer are exactly the same as those shared by the coder

## Code organization and readability
- [ ] Code file names are informative 
- [ ] It is clear in the code why tasks are being executed
- [ ] The code structure facilitates understanding of the tasks
- [ ] Code uses white space to improve readability
- [ ] There is extensive use of comments to explain the code
- [ ] The code is efficient (tasks are executed in the simplest way possible, loops are used when needed rather than repeating lines, pre-defined functions are used)
- [ ] Common tasks are abstracted and automated (e.g. using functions or macros)

## Clean dataset checks (pre-publication)
- [ ] The data does not include direct identifiers
- [ ] The dataset has a clearly labeled, uniquely and fully identifying ID variable(s)
- [ ] The level of observation of the data set is clear from the dataset name, ID variables, and documentation
- [ ] Variables have informative labels or an accompanying dictionary
- [ ] Categorical variables have clear and informative value labels
- [ ] No modification is made from the raw to the clean data other than correcting problems 
- [ ] No raw variables are processed (winsorized, for example)  
- [ ] Variables can be easily traced back to the original questionnaire
- [ ] Variables are sensibly ordered and dataset is compressed and saved in appropriate format

## Data cleaning tasks
- [ ] Are new variables being created in the cleaning do-files? 
- [ ] Are any changes being made to observations values in the cleaning do-files? 
- [ ] Check merges: Are any observations dropped? If so, is there a clear justification for that? If any observations didn't match, is that explained in the comments?
- [ ] Are missing values coded consistently? Are extended missing values used?
