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

Some of the steps in this guide can be done in multiple ways.
To keep the guide simple we will only mention one way per step.
Each time there are multiple ways we have chosen the one that,
based on our experience and testing,
is the easiest way that is not prone to errors.

## Prerequisites

These guidelines assumes that you:

1. Have a basic knowledge of SurveyCTO or ODK
1. Have access to a SurveyCTO server. You can set up a trial here (link)
1. Have SurveyCTO Desktop installed on your computer
1. Have a password manager that can handle secure notes (most do, here are our guidelines for setting up Last Pass) (add link to guidelines in this repo)

## Topic 1 - Creating and properly store a public/private key pair

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

### Step 1.1 - Creating a public/private key pair.

You can create the public/private key pair on your SurveyCTO server.
Log in to your server, and navigate to the _Design_ tab. Then click _Tools_.

image create 1

Then click _create a new key_ and then _Start key generator_

image create 2

Your keys will be downloaded in two files (one file for each key).
The name you enter in the next screen has no cryptographic function.
It will only be used to name the files that will be downloaded to your computer.
If you were to enter _name_of_my_project_ then your keys will be generated with these names:

* `name_of_my_project_Public.pem`
* `name_of_my_project_PRIVATEDONOTSHARE.pem`


We will store the keys in a password manager,
and then delete these files,
but give the key files a name so that you recognize them.

image create 3

When you download the keys,
make sure that they are not downloaded to a folder that is synced to,
for example, DropBox or OneDrive.
We do not want these keys to be sent to the cloud.
After we stored these keys in a password manager,
we want to delete these files from everywhere else,
and if they keys were already sent to the cloud,
then there is no way to fully delete them.


### Step 1.2 - Securely share and long term store the key pair

Saving the key pair in a regular folder your computer is not a secure enough way of storing the key files.
Instead our recommendation is that the key is stored in a password manager. Make sure that you have a password manager set up and that you are comfortable using it before proceeding with these instructions. We will provide instructions for the password manager LastPass, but this can be done in other password managers too. A secure alternative to saving to storing the keys in a password manager is to store the keys in an encrypted folder (link veracrypt) on your computer, but then you still need to store the key to the encrypted folder in a password manager.

Go to lastpass.com, log in to your vault and
click the plus sign in the red circle to create a new item.
Select _Secure Note_

image store 1

Then copy all the content of both keys you created and downloaded from your SurveyCTO server.
Make sure that you copy all content including the headers `-----BEGING PUBLIC KEY-----`. See example in the image below.

You should also make sure that you give a good name to your secure note with your key.
This key is likely to be stored for years and
the name you give the key should make sense to you and to all other team members -
both current and future - in this project.

If you are using LastPass for many keys and passwords,
then it is good to organize all your secure items in folders.

image store 2

### Step 1.3 - Delete the key files from your computers hard drive

A system of encryption is only as strong as its weakest link.
There is therefore no point in storing the keys safely in a passwords manager,
if we also stored it on our computers.
So the next step is to make sure that you have deleted the two key files from your computer.
Make sure to permanently delete them from your system by also emptying the _Recycle Bin_ (Windows) or the _Trash_ (Mac).

## Topic 2 - Using your public key to encrypt your data in SurveyCTO
### Encryption method A - Online form builder
### Encryption method B - Excel sheet form definition
## Topic 3 - Publishable fields
## Topic 4 - Using your private key to decrypt your data in SurveyCTO
## Topic 5 - Testing your setup before