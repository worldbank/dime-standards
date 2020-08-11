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

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-create-1.png" width="50%"><!--- Image is read from master branch or use full URL-->

Then click _create a new key_ and then _Start key generator_

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-create-2.png" width="50%"><!--- Image is read from master branch or use full URL-->

Your keys will be downloaded in two files (one file for each key).
The name you enter in the next screen has no cryptographic function.
It will only be used to name the files that will be downloaded to your computer.
If you were to enter _name_of_my_project_ then your keys will be generated with these names:

* `name_of_my_project_Public.pem`
* `name_of_my_project_PRIVATEDONOTSHARE.pem`


We will store the keys in a password manager,
and then delete these files,
but give the key files a name so that you recognize them.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-create-3.png" width="50%"><!--- Image is read from master branch or use full URL-->

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
Instead our recommendation is that the key is stored in a password manager.
Make sure that you have a password manager set up and
that you are comfortable using it before proceeding with these instructions.
We will provide instructions for the password manager LastPass,
but this can be done in other password managers too.
A secure alternative to saving to storing the keys in a password manager
is to store the keys in an encrypted folder (link veracrypt) on your computer,
but then you still need to store the key to the encrypted folder in a password manager.

Go to lastpass.com, log in to your vault and
click the plus sign in the red circle to create a new item.
Select _Secure Note_

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-store-1.png" width="50%"><!--- Image is read from master branch or use full URL-->

Then copy all the content of both keys you created and downloaded from your SurveyCTO server.
Make sure that you copy all content including the headers `-----BEGING PUBLIC KEY-----`. See example in the image below.

You should also make sure that you give a good name to your secure note with your key.
This key is likely to be stored for years and
the name you give the key should make sense to you and to all other team members -
both current and future - in this project.

If you are using LastPass for many keys and passwords,
then it is good to organize all your secure items in folders.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-store-2.png" width="50%"><!--- Image is read from master branch or use full URL-->

### Step 1.3 - Delete the key files from your computers hard drive

A system of encryption is only as strong as its weakest link.
There is therefore no point in storing the keys safely in a passwords manager,
if we also stored it on our computers.
So the next step is to make sure that you have deleted the two key files from your computer.
Make sure to permanently delete them from your system by also emptying the _Recycle Bin_ (Windows) or the _Trash_ (Mac).

## Topic 2 - Using your public key to encrypt your data in SurveyCTO

So far we have only prepared and properly stored
the cryptographic information we need to encrypt our data at rest,
but nothing is yet encrypted.
You can only encrypt a questionnaire when you create a new form on SurveyCTO's server.
If you already have a form on your server that you want to encrypt,
then you will have to copy the existing form to a new form,
and encrypt the new form at the time of creating it.
There are two methods to encrypt a SurveyCTO form.
If you are developing your form in Excel, then you should use method B.

### Encryption method A - Online form builder

Go to the _Design_ tab in your SurveyCTO server. Click _Start new form_.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-1.png" width="50%"><!--- Image is read from master branch or use full URL-->

Then give your new form a name and make sure that the checkbox "_Do you want this form's data to be encrypted?_" is checked. Then click _Next_.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-a1.png" width="50%"><!--- Image is read from master branch or use full URL-->

Then select "_Paste public key text:_",
and then go to your secure note in your password manager and copy the public key.
Make sure that you only copy the public key,
and make sure that key header `-----BEGIN PUBLIC KEY-----`
and the key footer `-----END PUBLIC KEY-----` are included.
Then click _Next_ and then complete your form.
SurveyCTO will test that there are no errors in the public key,
but you should never start collecting data using an encrypted form before
you have followed our test instructions below.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-a2.png" width="50%"><!--- Image is read from master branch or use full URL-->

### Encryption method B - Excel sheet form definition

In your Excel file where you are developing your SurveyCTO form,
go to the settings tab.
In the settings tab there is a column called `public_key`.
Paste the value of the public key in the cell in the first row of that column.
In this method it is important that you do **not** include
the  key header `-----BEGIN PUBLIC KEY-----`
and the key footer `-----END PUBLIC KEY-----`. See example below.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-b1.png" width="50%"><!--- Image is read from master branch or use full URL-->

Go to the _Design_ tab in your SurveyCTO server. Click _Upload form definition_.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-1.png" width="50%"><!--- Image is read from master branch or use full URL-->

Upload the form you just added the public key to the settings tab in,
and then follow the instructions as normal.
SurveyCTO will test that there are no errors in the public key,
but you should never start collecting data using an encrypted form before
you have followed our test instructions below.

## Topic 3 - Publishable fields

One often overseen feature when encrypting forms are publishable fields.
Publishable fields are fields for which
the collected data remain unencrypted even when the form is encrypted.
This data can be downloaded without providing the public key.

Here is one example where publishable fields can be useful.
Let's say you have hired a survey firm to collect data.
This survey firm wants to be able to download data from the SurveyCTO server to track progress,
but the IRB of your project does not allow you to share the respondents data with the survey firm.
It is unlikely that the survey firm needs all data to track progress,
and often you do not need any respondent data other than respondent ID
and survey meta data such as consent, completion, revisit info etc.
In this case you decide together with the survey firm
which is the minimum list of fields that they need to track progress.
If all of these variables are _not_ sensitive (which often is the case)
then you can make all of them publishable.
Then you can give the survey firm permission to download data from the server
or view it in the Data Explorer,
but as long as they do not have access to the private key,
they have no access to fields that not publishable.

To make a field publishable, you simply write "_yes_" in the _publishable_ column in the _survey_ tab in the questionnaire form.

To download the publishable data, go to the _Export_ tab in your SurveyCTO server.
Find your form and click "_Download for data_".
Then in the two sections as normal,
but in the "_Fields to include_" make sure that the checkbox
"_Publishable fields only (if you don't have the private key)_" is checked.
Then click _Download .csv now_.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-publish-1.png" width="50%"><!--- Image is read from master branch or use full URL-->

## Topic 4 - Using your private key to decrypt your data in SurveyCTO

Technically you can download encrypted data from your SurveyCTO server using a browser,
but then you first need to save your private key in a file on your computer.
And in the workflow we recommend,
you really want to avoid to ever store the private key in a file on your computer
after you have saved it in a password manager.
Instead, we recommend you to only download data using SurveyCTO Desktop (link to desktop)
as you can copy your key from your password manager and paste it
without having to save it in a file first.

In SurveyCTO Desktop you log in to your server,
and click _Sync_ in the menu to the left.
Fill in the information as normal,
but in step 2 you need to paste the key. See image below.
Go to your password manager and copy your private key.
Remember to include the header `-----BEGIN RSA PRIVATE KEY-----`
and the footer `-----END RSA PRIVATE KEY-----`.
Once you have copied it to your clipboard
(ctrl-C on Windows and command-C on Mac)
then simply click the _PASTE KEY_ button in SurveyCTO Desktop.
If the key you pasted is on the excepted format,
then you will see a green checkmark
and the text "_Private key successfully pasted_".
However, SurveyCTO has not tested if you pasted the correct key,
it will only test that when you are actually downloading data.
If you have pasted the incorrect key, then you will get an error
and you will not be able to read the data.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-sync-1.png" width="50%"><!--- Image is read from master branch or use full URL-->

## Topic 5 - Testing your setup before

Testing your encryption and decryption workflow is easy
but we cannot stress enough how important it is that
you do indeed test the workflow before you start to collect real data.

The first thing you want to make sure that your form is indeed encrypted.
The easiest way to do that is to log in to your server and go to the _Design_ tab.
Find your survey and see if the icon for encryption is an open or closed pad lock.
See the examples below where the form named _encrypted_form_ has a closed padlock
and the form named _unencrypted_form_ has an open padlock.
IF the padlock is closed then you know that all fields that
are **not** listed as publishable will be encrypted during data collection.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-test-1.png" width="50%"><!--- Image is read from master branch or use full URL-->

However, there is a second things you really want to test,
and that is to make sure you are able to decrypt the encrypted data.
To test your that you can decrypt data,
simply submit one mock data submission,
then copy the private key from your password manager,
and use SurveyCTO Desktop to download your mock submission.
If you are able to see the data that was collected in encrypted fields,
then you know that you will also be able to decrypt real data
once you starting to collect it.
