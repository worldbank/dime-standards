# Data analysis code review checklist

**Data source/survey round:**

**Date:**  

## List of files to be checked 
_Add names or links_:
- Master script
- Analysis scripts (list by order of priority)
- List of outputs

## List of auxiliary documents
- Documentation
- Compiled outputs (Eg: paper, presentation etc.)

## Reproducibility
- [ ] All scripts run from the master after adding the correct folder path to line(s) X (and XX)
- [ ] The master script is organized in a way that allows you to understand the general tasks being performed in the code
- [ ] The master script tracks which scripts create and use which files
- [ ] All the outputs are recreated and are exactly the same as the ones shared by the coder

## Code organization and readability
- [ ] Code file names are informative and/or link directly to outputs
- [ ] It is clear in the code why tasks are being executed
- [ ] The code structure facilitates understanding of the tasks
- [ ] Code uses white space to improve readability
- [ ] There is extensive use of comments to explain the code
- [ ] The code is efficient (tasks are executed in the simplest way possible, loops are used when needed rather than repeating lines, pre-defined functions are used)
- [ ] Common tasks are abstracted and automated (e.g. using functions or macros)

## Analysis scripts
- [ ] No variables are created in analysis scripts unless very specific to a particular output
- [ ] Code is modular, such that individual outputs can be run in any order
- [ ] Research decisions (e.g. sample used, treatment of missing variables) are well documented and the code implements them as described
- [ ] The code implements the models as described in the documentation
- [ ] The functions used are apropriate for the analysis being performed
- [ ] Categorical variables are used correctly (i.e. not used as continuous variables)
- [ ] Outputs are exported in a reproducible manner, and manual formatting is very limited
- [ ] Variable definitions are consistent across analyses
- [ ] Samples are consistent across analyses
- [ ] Models are consistent across analyses (e.g., outcomes, controls, standard error treatment)

## Analysis outputs
- [ ] Tables and graphs contain detailed notes explaining the methods, such that exhibits can be read and understood on their own
- [ ] The methods described in notes correspond to those implemented in the code
- [ ] Output tables are [easy to interpret](https://dimewiki.worldbank.org/Checklist:_Submit_Table)
- [ ] Output graphs are [easy to interpret](https://dimewiki.worldbank.org/Checklist:_Reviewing_Graphs)

