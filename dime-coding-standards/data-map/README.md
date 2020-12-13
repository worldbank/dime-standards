# DIME Data Map example

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

This example is based on fictive agriculture impact evaluation project
that collects data using household surveys and admin data from a government partner,
but this example applies to other types of projects as well.

## Data Linkage Table

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

| data_source | data_set_name | frequency | unit_of_obs | master_project_id | alternative_id | one_to_many_id | many_to_one_id | file_location | raw_backup_location_1 | raw_backup_location_2 | notes |
|-|-|-|-|-|-|-|-|-|-|-|-|
| admin data from government partner | farmer listing | once | farmer | hhid | gov_hh_id |  | comid |  |  | Hard drive in safe |  |
| listing | community listing | once | community | comid |  | | hhid |  |  |  |  |
| listing | household listing | once | farmer | hhid |  | comid |  |  |  |  |  |
| baseline survey | baseline prices | once | community | comid |  | | hhid |  |  |  |  |
| baseline survey | farmer baseline | once | farmer | hhid |  | comid |  |  |  |  |  |
| monitoring | monitoring data | monthly | farmer | hhid |  | comid |  |  |  |  |  |
| midline survey | midline prices | once | community | comid |  | | hhid |  |  |  |  |
| midline survey | farmer midline | once | farmer | hhid |  | comid |  |  |  |  |  |
| endline survey | endline prices | once | community | comid |  | | hhid |  |  |  |  |
| endline survey | farmer endline | once | farmer | hhid |  | comid |  |  |  |  |  |

Remarks about the data linkage table above:

* Note that the farmer listing data has two IDs. Research projects should have project IDs and a government ID. We need to list both here, but a research project should not

## Master Data settings

## Data Flow Chart
