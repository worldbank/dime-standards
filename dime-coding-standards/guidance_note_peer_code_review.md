# QUARTERLY PEER CODE REVIEW
# Guidance Note for World Bank Staff and Consultants

## Overview
Every quarter, DIME Analytics organizes the **Peer Code Review**, which is a real-time code and
data-quality assurance process. This is a structured opportunity for participants to exchange, run,
and provide feedback on each other’s code. Apart from increasing reproducibility, transparency and
adherence to best practices, it is a great learning opportunity - code writers get to look at their work
from a different perspective, and reviewers are exposed to different styles and practices.

The peer code review is designed for scripts that are modular enough to be understood on their own
(a reviewer can understand the script without having to refer to other project code files) and are short
enough for a reviewer to read through in **no more than 1 day** (depending on complexity). We
recommend submitting recently-completed tasks, to allow corrections to be made in real time.

The time commitment for each quarter is **8-10 hours**, including two dedicated sessions that participants are expected to attend. The remaining rounds of peer code review for FY25 are scheduled as follows:
1. **Week of November 4, 2024**
2. **Week of February 3, 2025**
3. **Week of June 2, 2025**

## How it works
1. Teams [sign up](https://survey.wb.surveycto.com/collect/code_review_sign_up?caseid=) to participate in the code review each quarter. All DIME Research Assistants
working on code are expected to participate regularly, and any Bank staff or consultant who would like to
get feedback on their code is welcome to participate.
2. Participants are paired for the review based on preferred statistical software and length of code.
3. All participants prepare a code package to share with assigned code review partners, following [these guidelines](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/Peer%20Code%20Review%20Submission%20Checklist.pdf). Submitted code should ideally be **no longer than 1000 lines** excluding the [main script.](https://github.com/worldbank/wb-reproducible-research-repository/blob/main/resources/main.do)
    - As part of this step, teams should identify and indicate which tasks they want reviewed. Examples include data cleaning, indicator construction, analysis, sampling and randomization, high-frequency checks, etc.
    - Teams should also specify if they want the reviewer to assess **computational reproducibility**.
    - Verifying computational reproducibility consists of ensuring that the reviewer can reproduce exactly the outputs (statistical tables and/or data visualizations) in the submitted package by running the exact package of code and data shared with the reviewer.
    - Further, in order to assess reproducibility, the submission package must include a **de-identified** version of the dataset - otherwise the code will not be eligible for verification of computational reproducibility.
4. The actual peer code review activity takes place over the course of one week, which includes:
   - A hybrid **kickoff session** to outline the process, and assign code review partners
   - A hybrid **group review session** with technical support from DIME Analytics. Pairs work together, and answer questions to allow each other to review their submitted code.

5. Reviewers review the code using the following resources:
   - **All packages:** [Main Feedback Checklist](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/Reviewer%20Feedback%20Checklist.pdf)
   - **Task-specific:**
     - [Cleaning checklist](https://github.com/worldbank/dime-standards/blob/d9111654531319fe96095d4bf0acf7fa0b66bacd/dime-coding-standards/checklists/Cleaning%20Code%20Review%20Checklist.pdf)
     - [Construction checklist](https://github.com/worldbank/dime-standards/blob/d9111654531319fe96095d4bf0acf7fa0b66bacd/dime-coding-standards/checklists/Construction%20Code%20Review%20Checklist.pdf)
     - [Analysis checklist](https://github.com/worldbank/dime-standards/blob/d9111654531319fe96095d4bf0acf7fa0b66bacd/dime-coding-standards/checklists/Analysis%20Code%20Review%20Checklist.pdf)
     - [Sampling and randomization checklist](https://github.com/worldbank/dime-standards/blob/d9111654531319fe96095d4bf0acf7fa0b66bacd/dime-coding-standards/checklists/Sampling%20and%20Random%20Treatment%20Assignment%20Checklist.pdf)
     - [HFCs checklist](https://github.com/worldbank/dime-standards/blob/d9111654531319fe96095d4bf0acf7fa0b66bacd/dime-coding-standards/checklists/HFCs%20Checklist.pdf)
       
6. Reviewers get one week to submit feedback using [this form](https://survey.wb.surveycto.com/collect/code_review_summary?caseid=), and upload completed task-specific checklists.

## What teams receive
- **Within 10 days**, TTLs and research assistants receive the following: a [standardized report](https://github.com/worldbank/dime-standards/blob/d9111654531319fe96095d4bf0acf7fa0b66bacd/dime-coding-standards/checklists/samples/Sample%20TTL%20Report.pdf) for their project indicating adherence to best practices and areas for improvement 
- Research assistants also receive detailed feedback through the task-specific checklists submitted by the reviewers
- All participating TTLs and DIME Managers also receive a [summary report](https://github.com/worldbank/dime-standards/blob/d9111654531319fe96095d4bf0acf7fa0b66bacd/dime-coding-standards/checklists/samples/Peer%20Code%20Review%20Summary%20-%20FY24%20Q3.pdf) highlighting common strengths and weaknesses. 
