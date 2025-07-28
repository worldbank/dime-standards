
## Peer Code Review – Reviewer Feedback Checklist

This checklist lists important factors to consider while reviewing your code review partner’s code package. Please use this checklist while reviewing the code package. 

Your deliverable from this exercise will be [this online survey form](https://survey.wb.surveycto.com/collect/code_review_summary?caseid=) which replicates the checklist below.



## Overview – First Impression
Once you have received a package from your code review partner, please check for the following general recommended practices:

- [ ] Data cleaning, variable creation, and analysis are done in **separate scripts**
- [ ] Analysis scripts do not include data processing, unless necessary for creating a table or graphic
- [ ] Each script is fully modular - that is to say that the scripts can be run independently from the master script, and do not depend on having the results of other scripts in memory.
- [ ] All scripts are well-commented
- [ ] All scripts are well-organized and formatted, such that one can easily identify functional chunks of code and evaluate whether they correctly implement the econometric or statistical process described
- [ ] Tables and charts are exported (preferably as **raw text files**)



##  Computational Reproducibility  
*(Applicable only if de-identified data was shared)*

**Next step:** If you received data as part of the peer review package, attempt to run the code files.
Ideally, you will be able to do so by changing only the top-level directory in the main script. Take
note of any issues in reproducing code outputs (constructed indicators, cleaned data, graphs, and
tables) as you will need to record them in this review summary form.

- [ ] I was able to run all code files in the package  
- [ ] Code did not run initially, but I identified the reason  
- [ ] Outputs (if any) reproduced exactly  
- [ ] Outputs did not reproduce, but I determined the reason



## Ease of Use and Understanding
**Now**, assess how easy it is to understand the code you are reviewing. Consider whether the documentation
provided is sufficient, and whether the code is organized in such a way that it would be
easy for someone else to work on it.

- [ ] I understood the code using the README and documentation  
- [ ] The code is organized so that core tasks can be edited in one place  
- [ ] The code is well structured, making it easy to update key tasks or parameters by modifying a single section rather than multiple parts of the codebase. 
- [ ] Estimated number of days needed to understand the code: `__`



##  Coding Practices  
*Check all that apply and note whether implementation was complete or needs improvement*

- [ ] Master script  
- [ ] Use of comments  
- [ ] Documentation  
- [ ] Folder organization  
- [ ] Consistent variable and file naming  
- [ ] Organized code structure (clear input/output tracking)  
- [ ] Use of white space  
- [ ] Use of loops/functions (e.g., `map`, `apply`, `sapply`)  
- [ ] Abstraction - using functions to do commonly repeated tasks



## ️ Final Comments
Finally, make note of the main strengths of the code, suggestions on how the coder can improve,
and any additional feedback from your side. You will need to provide this information in this detailed
review summary form.

1. **Three main strengths of the code reviewed:**  
   *(e.g., efficient scripts, proper use of loops, modular structure)*
   
   `______________________________________`
   
   `______________________________________`
   
   `______________________________________`
   

2. **Suggestions on how the coder can improve:**  
   *(e.g., use loops, simplify with functions, add version control with `ieboilstart`)*
   
   `______________________________________`

3. **Any additional feedback for the coder:**  
   *(e.g., improve folder structure, reproducible output tips, fix specific issues)*
   
   `______________________________________`
