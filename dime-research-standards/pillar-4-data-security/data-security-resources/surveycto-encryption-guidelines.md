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

## Creating and properly store a public/private key pair

SurveyCTO uses asymmetric encryption (link) where there are two keys called the public and the private key.
In SurveyCTO the public key is used to encrypt your data and the private key is used to decrypt your data.
As the names suggests it is very important that you keep your private key secret.
If you accidentally publish your private key, then your data is no longer securely protected.
And if you lose access to your private key, then there is in no way possible to decrypt your data.

There is no security risk of accidentally publishing your public key.
If you were to lose your public key, then you will not be able to encrypt any more data
(until you create a new public/private key pair)
but as long as you have the private key you will still be able to decrypt data encrypted with the lost public key.

Each public/private key pair is unique and no other private key can decrypt the data you encrypted with your public key.
You should not use the same key pair for all your project,
but you do not need to create a new key pair for each form.
We think that a good balance is to use one key pair for each project.
So multiple forms in the same project can use the same key,
but the same key should not be used across projects.
