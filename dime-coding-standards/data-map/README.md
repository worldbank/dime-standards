# DIME Data Map Example

This is an example of a Data Map.
This data mock data but based on a typical impact evaluation project at DIME,
but this framework should work on any research project
that use data from more than one source.

For a more general discussion on DIME's data map framework,
see the data map article on our wiki page: https://dimewiki.worldbank.org/wiki/Data_Map

You can also read about how a data map fits in the data workflow
in a typical research project in Chapter 3 in DIME data handbook
[Development Research in Practice](https://worldbank.github.io/dime-data-handbook/).

## Mock example background

This example is based on fictive agriculture impact evaluation project that we will call ProjectIE.
In ProjectIE there are two types of data sources.
Data acquired by household surveys and admin data shared by a government partner,
There are two units of observation used; community and farmer.
The intervention in this impact evaluation is a training that is offered to the farmer in the treatment group.
The random treatment assignment was done clustered at community level,
so all the farmers in the same community has the same treatment assignment.

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

| data_source                        | data_set_name     | frequency | unit_of_obs | master_project_id | alternative_id | one_to_many_id | many_to_one_id | file_location                                | raw_backup_location_1                             | raw_backup_location_2                     | notes |
|------------------------------------|-------------------|-----------|-------------|-------------------|----------------|----------------|----------------|----------------------------------------------|---------------------------------------------------|-------------------------------------------|-------|
| admin data from government partner | farmer listing    | once      | farmer      | hhid              | gov_hh_id      |                | comid          | data/encrypted/admindata/farmers.xlsx        | OneDrive : projectIE/data/farmers.xlsx            | Backed up with partner                    |       |
| listing                            | community listing | once      | community   | comid             |                |                | hhid           | data/listing/communities.csv                 | OneDrive : projectIE/data/communities.csv         | Hard drive labeled ProjectIE in PI's safe |       |
| baseline survey                    | baseline prices   | once      | community   | comid             |                |                | hhid           | data/baseline/raw/bl-price-survey.csv        | OneDrive : projectIE/data/bl-price-survey.csv     | Same as _community listing_ data          |       |
| baseline survey                    | farmer baseline   | once      | farmer      | hhid              |                | comid          |                | data/encrypted/baseline/raw/bl-hh-survey.csv | OneDrive : projectIE/data/bl-hh-survey.csv        | Same as _community listing_ data          |       |
| monitoring                         | monitoring data   | monthly   | farmer      | hhid              |                | comid          |                | data/monitoring/training-attendence.csv      | OneDrive : projectIE/data/training-attendence.csv | Same as _community listing_ data          |       |
| midline survey                     | midline prices    | once      | community   | comid             |                |                | hhid           | data/midline/raw/ml-prices-survey.csv        | OneDrive : projectIE/data/ml-prices-survey.csv    | Same as _community listing_ data          |       |
| midline survey                     | farmer midline    | once      | farmer      | hhid              |                | comid          |                | data/encrypted/midline/raw/ml-hh-survey.csv  | OneDrive : projectIE/data/ml-hh-survey.csv        | Same as _community listing_ data          |       |
| endline survey                     | endline prices    | once      | community   | comid             |                |                | hhid           | data/endline/raw/el-prices-survey.csv        | OneDrive : projectIE/data/el-prices-survey.csv    | Same as _community listing_ data          |       |
| endline survey                     | farmer endline    | once      | farmer      | hhid              |                | comid          |                | data/encrypted/endline/raw/el-hh-survey.csv  | OneDrive : projectIE/data/el-hh-survey.csv        | Same as _community listing_ data          |       |

Remarks about the data linkage table above:

* Note that the farmer listing data has two IDs.
Research projects should have project IDs and a government ID. We need to list both here,
but a research project should not use an external ID if the data contains confidential data.
* Only the raw datasets needs to be listed here.
The code documents how derivative datasets relates to these datasets.
* If your raw datasets includes confidential inform (such as PII), then it need to be encrypted.
A benefit of the data linkage table is that
it is also documented to people that does not have access to the encrypted folder
that the raw dataset is saved there.
* Confidential should be encrypted by the project team when backed up
unless it is either on a hard drive locked into a safe,
or if your IT department has set up a secure sync service
(see out guidelines for World Bank OneDrive
[here](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/onedrive-backup-guidelines.md).)

## Master datasets

In ProjectIE there are two unit of observations in the data linkage table
- community and farmer -
and we therefore need master datasets for both of them.
These master datasets should include all observations of these two units
that the research team ever interact with.
Note that this is often includes more observations than what are included in your analysis sample.
Examples of this could in the ProjectIE be farmers listed in the government partner's admin data
that were selected to be a part of the sample,
or farmers that are not in your study and but who attended the training
offered to the treatment group anyways and are included in the monitoring data.

#### Farmer master dataset

| hhid  | comid | first_name | last_name | gender | age | in_sample | attended_training |
|-------|-------|------------|-----------|--------|-----|-----------|-------------------|
| 10201 | 102   | Seana      | Sonschein | Female | 43  | 1         | 0                 |
| 10203 | 102   | Jermayne   | Zarb      | Male   | 38  | 1         | 0                 |
| 10205 | 102   | Emeline    | Faraker   | Female | 64  | 1         | 1                 |
| 10401 | 104   | Didi       | Frazer    | Female | 63  | 1         | 0                 |
| 10402 | 104   | Marchall   | Rives     | Male   | 40  | 0         | 0                 |
| 10403 | 104   | Lorinda    | Gabits    | Female | 50  | 1         | 1                 |
| 20701 | 207   | Sid        | Sorrie    | Male   | 43  | 1         | 0                 |
| 20702 | 207   | Pall       | Denacamp  | Male   | 62  | 1         | 1                 |
| 20704 | 207   | Mei        | Kezar     | Female | 35  | 0         | 1                 |
| 21401 | 214   | Cos        | Gronno    | Male   | 40  | 1         | 0                 |
| 21402 | 214   | Yorgo      | Adin      | Male   | 64  | 1         | 0                 |
| 21404 | 214   | Annamaria  | Cavozzi   | Female | 59  | 1         | 0                 |
| …     | …     | …          | …         | …      | …   | …         | …                 |

This is an exert of the master dataset that lists all the farmers the research team for ProjectIE ever interacted with. Most of this farmer is in the sample for this study but not all. Note thate treatment assignment is not included in this master dataset. As described above, treatment in this fictional study was randomly assigned on community level, so treatment status will be included in the community master dataset. To the

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

## Data Flow Chart
