## Peer Code Review - High-Frequency Checks Checklist

---

### **Reviewer Details**
- **Reviewer Name:**  
- **Coder Name:**

> **Note:** Please complete this checklist **only** if the submission includes **High-frequency checks**.

---

### **High-Frequency Checks (HFCs)**

This checklist focuses on reviewing the key outputs of high-frequency checks to ensure data quality.  
It highlights critical components of HFCs, but some sections may not apply to the specific checks you are reviewing.  
If the code also includes cleaning, construction, or analysis, please refer to the respective checklists [here](https://github.com/worldbank/dime-standards/tree/master/dime-coding-standards/checklists).

Once completed, please submit this checklist as an attachment along with [this form](https://survey.wb.surveycto.com/collect/code_review_summary?caseid=).

---

### **General**
- [ ] The data shared does not contain any personally identifying information (PII).  
- [ ] All scripts run from the main script after adding the correct folder path to line(s) X (and XX).  
- [ ] The code generates a tracking sheet or dashboard to monitor survey progress.  
- [ ] The tracking system updates automatically with new data, rather than requiring manual inputs.

---

### **Survey Progress Checks**

#### **Response Rates**
- [ ] The total number of surveys attempted, completed, and declined is reported.  
- [ ] Response rates are disaggregated by day and enumerator.  
- [ ] Decline reasons are categorized and summarized.

#### **Interview Duration**
- [ ] The average duration of interviews is reported.  
- [ ] Interview duration is broken down by module/section.  
- [ ] Unusually short or long interviews are flagged for review.

---

### **Survey Quality Checks**

#### **Duplicate & Consistency Checks**
- [ ] Duplicate entries in ID variables are identified and flagged.  
- [ ] If duplicates exist, non-ID variables are checked for differences.

#### **Missing Data & Outlier Checks**
- [ ] Missing values for key variables are reported.  
- [ ] Extended missing responses (Do not know, Refuse to answer) are summarized.  
- [ ] Continuous variables are checked for outliers and extreme values.

#### **Inconsistency Checks**
- [ ] Inconsistent responses across related questions are flagged.  
- [ ] Inconsistencies over time (e.g., same respondent providing different answers in different waves) are reported.

#### **Survey Form Version Checks**
- [ ] The number of responses is reported by form version and date.  
- [ ] Any discrepancies in form versions are flagged.

---

### **Enumerator Performance Checks**

#### **Response Rates by Enumerator**
- [ ] The number/share of surveys attempted, completed, and declined is reported per enumerator.  
- [ ] The number of attempts per respondent is tracked per enumerator.

#### **Interview Duration by Enumerator**
- [ ] The average interview duration is reported for each enumerator.  
- [ ] The average duration per module is reported for each enumerator.

#### **Enumerator-Specific Missing Data & Outliers**
- [ ] Overall missing rates are reported by enumerator and question type.  
- [ ] Average missing rates for key variables (which may lead to skipped sections) are reported per enumerator.  
- [ ] Outlier distributions are reported for each key variable per enumerator.

#### **Inconsistency & Error Checks by Enumerator**
- [ ] Total number of inconsistent responses is reported for each enumerator.  
- [ ] The average number of inconsistencies per day is tracked.  
- [ ] Total flagged errors per enumerator are summarized.  
- [ ] The average number of flagged errors per day is reported.
