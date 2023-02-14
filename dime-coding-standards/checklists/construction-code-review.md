# Data construction code review checklist

**Data source/survey round:**

**Date:**  

## List of files to be checked
_Add names or links_:
- Master script
- Constructed dataset(s)
- Construction scripts (list by order of priority)

## List of auxiliary documents
- Documentation
- Main constructed variables to be checked

## Reproducibility
- [ ] All scripts run from the master after adding the correct folder path to line(s) X (and XX)
- [ ] The master script is organized in a way that allows you to understand the general tasks being performed in the code
- [ ] The master script tracks which scripts create and use which files

## Code organization and readability
- [ ] Code file names are informative 
- [ ] It is clear in the code why tasks are being executed
- [ ] The code structure facilitates understanding of the tasks
- [ ] Code uses white space to improve readability
- [ ] There is extensive use of comments to explain the code
- [ ] The code is efficient (tasks are executed in the simplest way possible, loops are used when needed rather than repeating lines, pre-defined functions are used)
- [ ] Common tasks are abstracted and automated (e.g. using functions or macros)

## Construction scripts
- [ ] Check creation of new variables. 
  - [ ] Do you understand how and why each variable is constructed? If not, indicate where more comments or documentation are needed.
  - [ ] Does the code match the variable definition in the documentation? 
  - [ ] Is the correct function being used?  
- [ ] Check merges (joins). Does the number of observations in the resulting data set change? If so, is there a clear justification for that? If any observations didn't match, the reason for this explained in the comments?
- [ ] Check collapses (summarises), reshapes (pivots), and groupwise calculations (`bys` and `egen` for example). 
  - [ ] How are missing values treated by these commands? If missings are treated as zero, is there an explanation for why that is?
  - [ ] How does the number of non-missing values in the resulting data compare to the original? 
  - [ ] How does the number of observations in the resulting data compare to the original? 
  - [ ] Does the sort order of the data affect the result? 
  - [ ] Is the number of observations correct and are the mathematics correct?
- [ ] Check winsorization or other techniques for handling outliers. 
  - [ ] Is the reason for the chosen transformation explained? 
  - [ ] Is there documentation explaining how parameters such as cutoff percentiles were chosen and why one or both tails were altered?
- [ ] Check treatment of missing values such as imputation of removal of observations. 
  - [ ] Is the reason for the chosen treatment explained? 
  - [ ] Are there cases where you think missing values are being created or replaced unintentionally?
- [ ] Is there always clear documentation of why observations are dropped, if any?

## Constructed dataset(s)
- [ ] Is the resulting dataset tidy (each row is an observation, each column is a variable, only one unit of observation is represented in the data)?
- [ ] Are variable names informative?
- [ ] Are variable and value labels informative?
- [ ] Are all labels grammatically correct and free of special characters?
- [ ] Is there clear documentation (variable dictionary, variable labels, value labels, notes, comments) about variable definition?
- [ ] Are dataset file names informative?
