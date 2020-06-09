# Data cleaning code review checklist

**Data source/survey round:**

**Date**  

## List of files to be checked [Add names or links]
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
- [ ] Code names are informative 
- [ ] It is clear in the code why tasks are being executed
- [ ] The code structure facilitates understanding of the tasks
- [ ] Code uses white space to improve readability
- [ ] There is extensive use of comments to explain the code
- [ ] The code is efficient (tasks are executed in the simplest way possible, loops are used when needed rather than repeating lines, pre-defined functions are used)
- [ ] Common tasks are abstracted and automated (e.g. using functions or macros)

## Construction scripts
- [ ] Do you understand how and why each variable is constructed? If not, indicate to the author where more comments are needed.
- [ ] Check merges. Are any observations dropped? If so, is there a clear justification for that? If any observations didn't match, is that explained in the comments?
- [ ] Check collapses. How are missing values treated?
- [ ] Check winsorization. Is the reason for winsorizing explained? Is there documentation explaning how the percentile was chosen and why one/both tails were winsorized?
- [ ] Check treatment of missing values. Are research decisions well documented? Are there cases where you think missing values are being created or replaced unintentionally?
- [ ] Check creation of new variables. Does the code match the variable definition in the documentation? Is the correct function being used?
- [ ] Is there always clear documentation of why observations are dropped, if any?

## Constructed dataset(s)
- [ ] Is the resulting data set tidy (each row is an observation, each column is a variable)?
- [ ] Are variable names informative?
- [ ] Are variable labels informative?
- [ ] Are value labels informative?
- [ ] Are all labels grammatically correct and free of special characters?
- [ ] Is there clear documentation (variable dictionary, variable labels, value labels, notes, comments) about variable definition?
- [ ] Are data set file names informative?
