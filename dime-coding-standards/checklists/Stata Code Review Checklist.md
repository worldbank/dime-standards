
# Stata Peer Code Review Checklist

Use this checklist to improve your own Stata coding practice or to guide your peer code reviews.


## Main Do-file Setup
    
- [ ] Includes `clear all` and `set more off` at the start.
- [ ] Sets core configurations (`version`, `matsize`, `varabbrev`) directly or via a wrapper (e.g., `ieboilstart`)
- [ ] Script runs from start to end after changing directory paths in one place only.
- [ ] Uses only **relative paths** (no `C:/...`) 
- [ ] Uses forward slashes in file path for OS compatibility
- [ ] Installs required packages or includes an `ado` folder with dependencies.
- [ ] Sets a **random seed** for reproducibility.
- [ ] Uses `run` or `do` to call modular scripts for cleaning, construction, etc.



    
## Data Management
    
- [ ] Dataset includes a **unique ID** and is sorted.
- [ ] Duplicate resolution is stable (does not use `duplicates drop, force`)
- [ ] Does not include PII or sensitive information.
- [ ] All variables are clearly labeled.
- [ ] Value labels are consistent (e.g., avoiding cases where varA: 1 = yes, 0 = no, but varB: 1 = yes, 2 = no).
- [ ] Extended missing values are used where applicable (e.g., `.d` for Do not know, `.r` for Refuse to answer, etc.).
- [ ] Sorting is consistently and uniquely enforced using `sort` or `gsort` before commands that depend on it
- [ ] Uses tempfiles instead of saving intermediate datasets unnecessarily.
- [ ] Saves final dataset only once, avoids repeated overwriting.
- [ ] Follows tidy data principles: one row per observation, one column per variable.
- [ ] Avoids interactive commands (`edit`, `browse`).

    
## Data Types & Variables
    
- [ ] String variables are only used when necessary (e.g., proper nouns or alphanumeric IDs).
- [ ] Converts categorical strings into labeled numeric variables (e.g., using `encode`)
- [ ] Date variables are stored in proper date formats (e.g., `%td`, `%tm`).


    
## Merge Checks
    
- [ ] No `m:m` merges used.
- [ ] Mismatches or dropped observations are explained `tab _merge` and `assert` checks.
- [ ] If any observations are dropped, a clear justification is provided in the code.

---
    
## Append Checks
    
- [ ] Variables being appended are of the same type and structure.
- [ ] Avoids `append, force`.
- [ ] Any new variables introduced in appended datasets are properly handled.


    
## Code Readability & Style
    
- [ ] Uses proper indentation inside loops or programs.
- [ ] Uses white space and line breaks `///` for long lines.
- [ ] Uses descriptive index names in loops/globals.
- [ ] Uses `${}` syntax for global macros.
- [ ] Comments clearly explain steps and analysis decisions.
- [ ] Each section is clearly marked (e.g., `*** SECTION: Construct Outcomes`).
- [ ] Avoids hardcoding values (uses macros).
- [ ] Avoids copy-pasting blocks; uses loops or programs where repetitive code appears.


    
## Variable Construction

- [ ] Each variable’s logic aligns with codebook or documentation.
- [ ] Transformations (log, winsorize, etc.) are justified and explained.
- [ ] Categorical variables are properly labeled and encoded.
- [ ] Data transformations are verified with `assert` or summary checks.


    
## Collapse / Group-wise Calculations
    
- [ ] Data is sorted uniquely before using `by: egen` or `by: gen`
- [ ] Aggregations like `sum`, `mean` are documented and correct.
- [ ] Missing values handled appropriately during `collapse`and `egen`.


    
## Output & Logging
    
- [ ] Output tables or graphs are generated using commands like `esttab`, `putexcel`, `asdoc`.
- [ ] Output files are clearly named and saved in dedicated folders.
- [ ] Log files are started with `log using` and closed with `log close`.
- [ ] Outputs are saved in plain text formats (e.g., `.csv, .txt, .tex`) to ensure compatibility with Git and facilitate version control.



## Reproducibility & Documentation
    
- [ ] Code runs from a clean slate, reproducibly.
- [ ] README documents required Stata version and packages.
- [ ] `ieboilstart` or equivalent ensures version stability.
- [ ] Folder and file structure is documented.
- [ ] README mentions the code line to be updated to run the code.


    