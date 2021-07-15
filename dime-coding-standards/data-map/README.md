# DIME Data Map Example

This is an example of using a data map to organize workflow in a project.
The mock data in this example is based on a typical impact evaluation project at DIME,
but this framework should work on any research project
that use data from more than one source.

For a more general discussion on DIME's data map framework,
see the data map article on our wiki page: https://dimewiki.worldbank.org/wiki/Data_Map

You can also read about how a data map fits in the data workflow
in a typical research project in Chapter 3 in DIME data handbook
[Development Research in Practice](https://worldbank.github.io/dime-data-handbook/).

## Mock example background

This example is based on a fictional agriculture impact evaluation project,
that we will call ProjectIE.
In ProjectIE, there are two types of data sources -
data acquired by household surveys, and admin data shared by a government partner.
Further, there are two units of observation - community and farmer.
The intervention for this impact evaluation is a training
that is offered to farmers in the treatment group.
The treatment assignment was done randomly by clustering at the community level,
so all the farmers in the same community have the same treatment assignment.

## Data linkage table

A data linkage table keeps track of the datasets and how they may be linked with each other.
A template for the table below can be downloaded from this repo both in
[Excel format](https://github.com/worldbank/dime-standards/blob/data-map/dime-coding-standards/data-map/templates/data-linkage-table-template.xlsx?raw=true)
or in [.csv format](https://github.com/worldbank/dime-standards/blob/data-map/dime-coding-standards/data-map/templates/data-linkage-table-template.csv?raw=true).

If you version control your data work using git,
we recommend storing your data linkage table in a csv format as it is suitable for git version control.
We provide the Excel file as well,
as that format is more straightforward to download form a GitHub repo.
To download the csv file,
you need to copy the content the browser into a file in a text editor
that you then save as a csv file.
Regardless how you download the file,
if you use git, then we strongly recommend using the .csv format
to version control you data linkage table as well.

#### ProjectIE data linkage table

| data_source                        | data_set_name     | frequency | unit_of_obs | project_id | alternative_id | one_to_many_id | many_to_one_id | file_location                                | raw_backup_location_1                             | raw_backup_location_2                     | notes |
|------------------------------------|-------------------|-----------|-------------|------------|----------------|----------------|----------------|----------------------------------------------|---------------------------------------------------|-------------------------------------------|-------|
| admin data from government partner | farmer listing    | once      | farmer      | hhid       | gov_hh_id      |                | comid          | data/encrypted/admindata/farmers.xlsx        | OneDrive : projectIE/data/farmers.xlsx            | Backed up with partner                    |       |
| listing                            | community listing | once      | community   | comid      |                |                | hhid           | data/listing/communities.csv                 | OneDrive : projectIE/data/communities.csv         | Hard drive labeled ProjectIE in PI's safe |       |
| baseline survey                    | baseline prices   | once      | community   | comid      |                |                | hhid           | data/baseline/raw/bl-price-survey.csv        | OneDrive : projectIE/data/bl-price-survey.csv     | Same as _community listing_ data          |       |
| baseline survey                    | farmer baseline   | once      | farmer      | hhid       |                | comid          |                | data/encrypted/baseline/raw/bl-hh-survey.csv | OneDrive : projectIE/data/bl-hh-survey.csv        | Same as _community listing_ data          |       |
| monitoring                         | monitoring data   | monthly   | farmer      | hhid       |                | comid          |                | data/monitoring/training-attendence.csv      | OneDrive : projectIE/data/training-attendence.csv | Same as _community listing_ data          |       |
| midline survey                     | midline prices    | once      | community   | comid      |                |                | hhid           | data/midline/raw/ml-prices-survey.csv        | OneDrive : projectIE/data/ml-prices-survey.csv    | Same as _community listing_ data          |       |
| midline survey                     | farmer midline    | once      | farmer      | hhid       |                | comid          |                | data/encrypted/midline/raw/ml-hh-survey.csv  | OneDrive : projectIE/data/ml-hh-survey.csv        | Same as _community listing_ data          |       |
| endline survey                     | endline prices    | once      | community   | comid      |                |                | hhid           | data/endline/raw/el-prices-survey.csv        | OneDrive : projectIE/data/el-prices-survey.csv    | Same as _community listing_ data          |       |
| endline survey                     | farmer endline    | once      | farmer      | hhid       |                | comid          |                | data/encrypted/endline/raw/el-hh-survey.csv  | OneDrive : projectIE/data/el-hh-survey.csv        | Same as _community listing_ data          |       |

#### Notes on this data link table

* In the table above, note that the farmer listing data has two IDs.
Research projects usually have both project IDs, as well as a government ID.
In this case, we need to list both these IDs,
but a research project should not keep an external ID in a de-identified dataset,
if the dataset contains confidential information.
* Only list the raw datasets in this table and not derived datasets.
However, make sure that your code clearly documents how derivative datasets relate to these datasets.
* If your raw datasets includes confidential information (such as PII),
then this information must be encrypted.
A benefit of the data linkage table is that
it is also available to people that do not have access to the encrypted folder.
* Confidential information should always be encrypted by the project team when backing up project data.
The only exception to this is if the data is either on an external hard drive
which is locked up in a safe,
or if your IT department has set up a secure sync service
(see our guidelines for using the World Bank OneDrive
[here](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/onedrive-backup-guidelines.md)).

## Master datasets

In ProjectIE, there are two units of observation in the data linkage table -
community and farmer.
Therefore, we need master datasets for each of these,
and each master dataset should include all observations
that the research team has ever interacted with.
Note that due to this definition,
the master datasets will often include more observations than are included in your analysis sample.
For example, in ProjectIE,
these additional observations could include farmers listed in the government partner's admin data
that were not selected to be a part of the sample.
Similarly, there could be farmers who were not included in your study sample,
but who treatment group training programs, and were therefore included in the monitoring data.

#### Farmer master dataset

| hhid  | comid | first_name | last_name | female | age | in_sample | attended_training |
|-------|-------|------------|-----------|--------|-----|-----------|-------------------|
| 10201 | 102   | Seana      | Sonschein | 1      | 43  | 1         | 1                 |
| 10203 | 102   | Jermayne   | Zarb      | 0      | 38  | 1         | 0                 |
| 10205 | 102   | Emeline    | Faraker   | 1      | 64  | 1         | 1                 |
| 10401 | 104   | Didi       | Frazer    | 1      | 63  | 1         | 0                 |
| 10402 | 104   | Marchall   | Rives     | 0      | 40  | 0         | 0                 |
| 10403 | 104   | Lorinda    | Gabits    | 1      | 50  | 1         | 1                 |
| 20701 | 207   | Sid        | Sorrie    | 0      | 43  | 1         | 0                 |
| 20702 | 207   | Pall       | Denacamp  | 0      | 62  | 1         | 0                 |
| 20751 | 207   | Mei        | Kezar     | 1      | 35  | 0         | 1                 |
| 21401 | 214   | Cos        | Gronno    | 0      | 40  | 1         | 1                 |
| 21402 | 214   | Yorgo      | Adin      | 0      | 64  | 1         | 1                 |
| 21404 | 214   | Annamaria  | Cavozzi   | 1      | 59  | 1         | 0                 |
| …     | …     | …          | …         | …      | …   | …         | …                 |

The above table is an excerpt of a master dataset that lists all farmers with
whom the research team for ProjectIE has ever interacted.
Typically most of these farmers are included in the sample for this study,
but not all of them have to be in the sample
as all observations this project interacts with should be listed here.
Note that we have not included treatment status in this master dataset.
As mentioned earlier,
treatment status in this fictional study was randomly assigned at the community level,
so treatment status will be included in the community master dataset (excerpt below).
However, since sampling for this project was done at the farmer level,
therefore sampling status has been included in this master dataset.

#### Community master dataset

| comid | community_name | region   | treatment |
|-------|----------------|----------|-----------|
| 102   | Lashite        | Koungin  | 1         |
| 104   | Ashiavrongo    | Koungin  | 0         |
| 108   | Wara           | Koungin  | 1         |
| 110   | Témebancoro    | Koungin  | 0         |
| 207   | Nibokro        | Sénénéga | 0         |
| 214   | Sikiali        | Sénénéga | 1         |
| 215   | Ifekka         | Sénénéga | 1         |
| 220   | Balenni        | Sénénéga | 0         |
| …     | …              | …        | …         |

The above table is an excerpt of all the communities
that are relevant for our example, that is, ProjectIE.
Since treatment was randomly assigned at the community level,
this master dataset is the authoritative source of information on treatment status,
even though farmers will be the unit of analysis for regressions in this study.

#### Notes on these master data sets

* It is common parctice to put the project ID as the leftmost columns,
but note that the master dataset does not govern what the project ID is -
that is governed by the data linkage table

#### Use master datasets to identify datasets without the project ID

If the research team receives a dataset without the project ID,
then they must merge these datasets with the master dataset for the relevant unit of observation.
For instance, suppose that our monitoring data was attendance sheets from the training sessions,
but it does not have any other identifier except full names and the community where they live.
Further, suppose that that we also want to merge treatment status with the monitoring data
to see if anyone in the control group had attended the trainings.
In this case, we would first have to merge the monitoring data with
the farmer master dataset using a string match.

Please note that we have to resolve all ambiguous string matches manually
to make sure that matches that are not exact are resolved correctly.
Note that we will do this string match for all farmers in the farmer master dataset,
and not just for the farmers we think might have attended
(that is, farmers in the treatment group).
In this case, including all farmers gives us the maximum amount of information
for resolving any unambiguous matches.

If we find any farmers that we do not have in our farmer master dataset,
then we should add them to the master dataset and assign them a project ID.
For example, see farmer with ID 20751 in the farmer master dataset.
This could be an example of a farmer who attended the training,
but was not in the sample.

Once we have performed the string match as accurately as possible,
we will have project IDs for both, farmers as well as the communities in the monitoring data.
Then we can easily merge this with the community master dataset to
get information on the treatment status.

## Data flow chart

While the data linkage table is an objective communication
on all the ways the datasets may correctly be linked,
the data flow chart is a normative communication
on the best way to combine the datasets to answer the research question.

The data flow chart below should be read from left to right.
Not that every starting point in the flow chart is either
a dataset in the data linkage table, or a master dataset.
This is very important, as the data flow chart is not unambiguous unless this is the case.

<img src="https://github.com/worldbank/dime-standards/blob/data-map/dime-coding-standards/data-map/img/data-flow-chart-example.png" width="75%"><!--- Image is read from master branch or use full URL-->

Creating a flow chart like this is a great tool for the project team to,
early on, make sure that they have a plan
for how to acquire all dataset they need to create the analysis data set.
Once this is agreed on then this is the best tool a PI can have
to communicate to the field team and the research assistants
what their vision for the data work is.
This is also a great tool to communicate across time what the plan is so that
project members that join in the middle of project can easily know
what has been decided on in meetings before they joined the team.

The flow chart above was made in the free online flow chart tool: https://app.diagrams.net/
