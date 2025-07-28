# PEER CODE REVIEW
# Guidance Note for World Bank Staff and Consultants

## Overview
DIME Analytics organizes the **Peer Code Review** as a real-time code and data-quality assurance process, providing a structured opportunity for participants to exchange, run, and provide feedback on each other's code. Beyond improving reproducibility, transparency, and adherence to best practices, it is also a valuable learning experience—code writers gain fresh perspectives on their work, while reviewers are exposed to different coding styles and practices.

The Peer Code Review is especially beneficial for **new Research Assistants**, as it helps them understand expectations and learn from others' code.

The review is designed for scripts that are modular enough to be understood on their own (i.e., a reviewer can follow the script without referring to other project files) and short enough to be reviewed **within one day** (depending on complexity). If participants wish to submit longer scripts, they will be paired with others submitting similarly long code to ensure a balanced review process. We recommend submitting recently completed tasks to allow for timely corrections and improvements.

Participants may choose to **only review**, **only submit**, or **do both**. Pairing will be based on availability, with **priority given to those who choose to both review and submit**. 

The time commitment for each round is **8-10 hours**, including two dedicated sessions that participants are expected to attend.

## How It Works

1. Teams [sign up](https://survey.wb.surveycto.com/collect/code_review_sign_up?caseid=) to participate in the code review.  
   - You can choose to **only review**, **only submit**, or **do both**.
   - Pairing is based on availability, with **priority given to those who opt to both review and submit**.
   - All DIME Research Assistants working on code are expected to participate regularly.  
   - Any Bank staff or consultant seeking feedback on their code is welcome to join.  
2. Participants are paired for the review based on their preferred statistical software and the length of their code.  
3. All participants prepare a code package to share with their assigned code review partners, following [this checklist](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/Peer%20Code%20Review%20Submission%20Checklist.md).  
   - Submitted code should ideally be **around 1,000 lines**, excluding the main scripts ([Stata](https://github.com/worldbank/wb-reproducible-research-repository/blob/main/resources/main.do), [R](https://github.com/worldbank/wb-reproducible-research-repository/blob/main/resources/main.R)).  
   - This is a recommendation rather than a strict limit—longer submissions are allowed but may require more time to review. In such cases, participants will be matched with others submitting similarly long code.  
   - Teams should specify which aspects of their code they would like reviewed, such as: Data cleaning, Indicator construction, Analysis, Sampling and randomization, High-frequency checks, etc.
   - Teams should also indicate whether they want the reviewer to assess **computational reproducibility**. Computational reproducibility verification ensures that the reviewer can reproduce the exact outputs (e.g., statistical tables, visualizations) using the submitted code and dataset.  
   - To enable reproducibility checks, the submission package **must** include a **de-identified dataset**. If no dataset is provided, the code will not be eligible for computational reproducibility verification.
4. The **peer code review** takes place over the course of two weeks and includes:  
   - A **hybrid kickoff session** outlining the process and assigning code review partners. Attendance is **optional** for those who have participated before.  
   - A **hybrid group review session** with technical support from DIME Analytics.  
     - Pairs work together, reviewing each other's code and addressing questions.  
     - Attendance is **mandatory**—if the scheduled session is not feasible, Analytics will facilitate an alternative meeting.  
   - This activity is most effective when teams can collaborate **in person**, allowing for real-time discussions and clarifications.  
5. Reviewers assess the code using the following resources:  
   - **General:** [Main Feedback Checklist](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/Reviewer%20Feedback%20Checklist.md)  
   - **Task-Specific Checklists:**  
     - [Cleaning Code Review Checklist](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/Cleaning%20Code%20Review%20Checklist.md)  
     - [Indicator Construction Checklist](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/Construction%20Code%20Review%20Checklist.md)  
     - [Analysis Code Review Checklist](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/Analysis%20Code%20Review%20Checklists.md)  
     - [Sampling & Randomization Checklist](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/Sampling%20and%20Random%20Treatment%20Assignment%20Checklist.md)  
     - [High-Frequency Checks Checklist](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/HFCs%20Checklist.md)  
6. Reviewers have one week to submit feedback using [this form](https://survey.wb.surveycto.com/collect/code_review_summary?caseid=) and upload their completed task-specific checklists.


## What teams receive
- **Within 10 days**, TTLs and research assistants receive the following: a [standardized report](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/samples/Sample%20Feedback%20Report.pdf) for their project indicating adherence to best practices and areas for improvement 
- Research assistants also receive detailed feedback through the task-specific checklists submitted by the reviewers
- All participating TTLs and DIME Managers also receive a [summary report](https://github.com/worldbank/dime-standards/blob/master/dime-coding-standards/checklists/samples/Peer%20Code%20Review%20Summary%20-%20FY24%20Q3.pdf) highlighting common strengths and weaknesses. 


### Peer Code Review Sessions Planned for FY26
The upcoming Peer Code Review sessions are scheduled for:

- Week of August 18, 2025
- Week of November 3, 2025
- Week of March 9, 2026