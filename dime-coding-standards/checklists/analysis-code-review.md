# Data cleaning code review checklist

**Data source/survey round:**

**Date:**  

## List of files to be checked 
_Add names or links_:
- Master script
- Analysis scripts (list by order of priority)
- List of outputs

## List of auxiliary documents
- Documentation
- Originally-created outputs

## Reproducibility
- [ ] All scripts run from the master after adding the correct folder path to line(s) X (and XX)
- [ ] The master script is organized in a way that allows you to understand the general tasks being performed in the code
- [ ] The master script tracks which scripts create and use which files
- [ ] All the outputs are recreated and are exactly the same as the ones shared by the coder

## Code organization and readability
- [ ] Code names are informative 
- [ ] It is clear in the code why tasks are being executed
- [ ] The code structure facilitates understanding of the tasks
- [ ] Code uses white space to improve readability
- [ ] There is extensive use of comments to explain the code
- [ ] The code is efficient (tasks are executed in the simplest way possible, loops are used when needed rather than repeating lines, pre-defined functions are used)
- [ ] Common tasks are abstracted and automated (e.g. using functions or macros)

## Analysis scripts
- [ ] No variables are created in analysis scripts unless very specific to a particular output
- [ ] Code is modular, such that individual outputs can be run in any order
- [ ] Research decisions are well documented in the code (e.g. sample used, treatment of missing variables)
- [ ] The code implements the models described in the documentation
- [ ] The functions used are apropriate for the analysis being performed
- [ ] Categorical variables are used correctly (i.e., labeled integers are not used as continuous variables)
- [ ] Outputs are exported in a reproducible manner, and manual formatting is very limited
