# DIME Analytics - Data Security Guides - SurveyCTO Encryption

[SurveyCTO](https://www.surveycto.com/) is a data collection software and service built on the open source tool ODK (add link).
Any time you collect data that includes confidential data you must encrypt your data.
The most common reason that data is confidential is that it include personal identifiers such as names.
SurveyCTO automatically encrypts your data _in transit_  (link wiki)
but to properly protect your data you also need to encrypt your data _at rest_ (link wiki).
**Encryption-in-transit** can be done properly without any input from the user and that is why this is automatic.
Proper **encryption-at-rest** is never automatic as the user may be the only one that has access to the decryption key.
That is why encryption at rest is not automatic and not enabled by default.
Handling the key is the user's responsibility and loosing the key means that there is no way of recovering the data.
This guide is DIME Analytics' best practice on how to encrypt data in SurveyCTO and how to securely handle the decryption key.


## Prerequisites

These guidelines assumes that you:

1. Have a basic knowledge of SurveyCTO or ODK
1. Have SurveyCTO Desktop installed on your computer
1. Have a password manager that can handle secure notes (most do, here are our guidelines for setting up Last Pass) (add link to guidelines in this repo)
