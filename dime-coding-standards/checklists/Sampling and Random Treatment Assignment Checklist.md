
## Peer Code Review – Sampling and Random Treatment Assignment Checklist

### Reviewer Details
- **Reviewer Name:**  
- **Coder Name:**  

> *Note: Please complete this checklist only if the submission includes sampling and/or randomization tasks.*



## Sampling and Randomization Tasks

This checklist highlights key aspects to review in your partner’s sampling and randomization code.

- **Sampling** refers to defining the sample frame, i.e., selecting which units (e.g., individuals, households) will be included in the study.  
- **Randomization** refers to assigning treatment and control groups within the sampled units.

Once completed, please submit it as an attachment along with [this form](https://survey.wb.surveycto.com/collect/code_review_summary?caseid=).

##  Sampling Checklist

This section focuses on reviewing the code that performs **sampling**.

### **Setting Parameters**
- [ ] Script sets the software version (e.g., `version` in Stata).
- [ ] A random seed is set for reproducibility (e.g., `set seed` in Stata or `set.seed()` in R).
- [ ] The seed is generated externally (e.g., from [random.org](https://www.random.org/integers/?num=1&min=100000&max=999999&col=5&base=10&format=html&rnd=new).
- [ ] The dataset is sorted by a unique identifier.

### **Sampling Methodology**
- [ ] Sampling strategy is clearly documented, including inclusion/exclusion criteria.
- [ ] Sampling method (e.g., stratified, clustered, or simple random sampling) is explicitly stated.
- [ ] Unequal cluster sizes are handled and justified.
- [ ] Probability weights, if used, are calculated and stored.

### **Defining the Sampling Frame**
- [ ] Dataset includes necessary variables for sampling (e.g., clusters, strata).
- [ ] **Advanced check**: Clusters, strata, and IDs do not contain any personally identifiable information
(PII).
- [ ] **Advanced check**: The resulting dataset is checked for stability using commands like `datasignature`,
file hashing, `assert`, and/or `isid, sort`.

### **Sampling Execution**
- [ ] Script outputs a dataset marking sampled vs. non-sampled units.
- [ ] Final sampling results are reproducible across multiple runs.
- [ ] If the sample is finalized for field use, a logic switch prevents accidental overwriting.
- [ ] Outputs include codebooks, value labels, and documentation.



##  Randomization Checklist

This section focuses on reviewing the code that performs **random treatment assignment**.

### **Setting Parameters**
Verify that the coding environment is properly configured to ensure reproducibility.

- [ ] Software or package version is specified (e.g., `version` in Stata or package version control in R).
- [ ] Random seed is set (e.g., `set seed` in Stata or `set.seed()` in R).
- [ ] Seed is externally generated (e.g., from [random.org](https://www.random.org/integers/?num=1&min=100000&max=999999&col=5&base=10&format=html&rnd=new).
- [ ] Dataset is sorted by a unique identifier before randomization.

### **Random Treatment Assignment**
- [ ] Treatment assignment is done using code (not manual methods).
- [ ] Method is well-documented (e.g., simple, block, stratified).
- [ ] Treatment/control variable is created with clear labels.
- [ ] No new observations are created during randomization.
- [ ] Randomization is reproducible and produces consistent results across multiple runs.
- [ ] Output includes treatment assignment dataset and documentation.
- [ ] If the treatment assignment is finalized for use, a logic switch prevents accidental overwriting.
