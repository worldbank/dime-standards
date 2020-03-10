# DIME Research Standards

## Pillar 1 - Research Ethics
For implementation resources, see the [Research Ethics Guidelines](https://github.com/worldank/dime-standards/blob/master/DIME-Research-Standards/pillar-1-research-ethics)

- Researchers must secure ethics approval from an institutional review board (IRB) and the appropriate authority in the study location, for studies directly involving human subjects or using personally-identifying information.
- All research team members that handle personally-identifiable information must have up-to-date Human Subjects Research Certification.
- Researchers must ensure confidentiality, privacy, and anonymity of study participants;
study participants must have the opportunity to provide informed consent, and revoke that consent at any time.

## Pillar 2 - Research Transparency
For implementation resources, see the [Research Transparency Guidelines](https://github.com/worldank/dime-standards/blob/master/DIME-Research-Standards/pillar-2-research-transparency)

- Researchers must register the study prior to receiving implementation funding.

##  Pillar 3 - Research Reproducibility
For implementation resources, see the [Research Reproducibility Guidelines](https://github.com/worldank/dime-standards/blob/master/DIME-Research-Standards/pillar-3-research-reproducibility)

- All projects will use GitHub to document data work.
- Research assistants will regularly participate in code review with their peers.
- All projects will have a [master script](https://dimewiki.worldbank.org/wiki/Master_Do-files) that runs all the other
scripts that are needed for the project, in order.
- *Computational Reproducibility* must be verified by DIME Analytics prior to publication for all DIME Working Papers
and academic publications.

##  Pillar 4 - Data Security
For implementation resources, see the [Data Security Guidelines](https://github.com/worldank/dime-standards/blob/master/DIME-Research-Standards/pillar-4-data-security)

- All personally-identifiable data must be stored and transferred securely, including in communication with field staff. 
  - All servers for data collection must be [encrypted](https://dimewiki.worldbank.org/wiki/Encryption) both
  in transit (sent over the internet) and at rest (stored on a web server).
    - Encryption at rest must be implemented so that no person not listed on the IRB ever has access to the decryption key or the unencrypted data. This includes server hosts or administrators, sharing or syncing service providers, internet providers, and staff not listed on the IRB at any institution.
  - All identified data must be stored only in securely encrypted locations,
  and must always be encrypted when shared, even if shared only within the project team (link to DIME Encryption Protocol)
  - World Bank PIs should back up raw data in a WB OneDrive folder that is not shared with anyone, and is not synced to any computer.
- The project team should create a [de-identified](https://dimewiki.worldbank.org/wiki/De-identification) copy of the
primary data before starting data cleaning and analysis,
removing most sensitive information (e.g. names) even if some identifying information
(e.g. geocoordinates) is required for analysis 

##  Pillar 5 - Data Publication
For implementation resources, see the [Data Publication Guidelines](https://github.com/worldank/dime-standards/blob/master/DIME-Research-Standards/pillar-5-data-publication)

- Prior to publication, the research team must remove all potential identifiers.
DIME Analytics can assist with assessing the risk of statistical disclosure.
- All DIME publications will have a replication package available, including a citation or reference to the data in the [World Bank Microdata Catalog](https://dimewiki.worldbank.org/wiki/Microdata_Catalog) and a GitHub repository containing the code required for replication of the paper.
- Researchers must complete a data publication plan, detailing the plan and timeline for publishing impact evaluation data,
and expected access restrictions. Data should be cataloged using the
[World Bank Development Data Hub](https://datacatalog.worldbank.org/) (DDH) -
either the Microdata Catalog or Geospatial feature.
