# DIME Analytics - Data Security Guides - SurveyCTO Encryption

[SurveyCTO](https://www.surveycto.com/) is a data collection software and service built on the open source software [Open Data Kit (ODK)](https://opendatakit.org/).
Any time you collect data that includes confidential information you must encrypt your data at all times.
The most common reason that data is confidential is that it includes direct personal identifiers such as names.
SurveyCTO automatically encrypts your data [in transit](https://dimewiki.worldbank.org/wiki/Encryption#Encryption_in_Transit),
but to properly protect your data you also need to encrypt your data [at rest](https://dimewiki.worldbank.org/wiki/Encryption#Encryption_at_Rest).
**Encryption-in-transit** doesn't require the user to have access to the decryption keys, which is why this can be made an automatic part of the service without any user action.
By contrast, **encryption-at-rest** is never automatic, because the user has to store and handle the decryption key.
Handling the key is the user's responsibility and losing the key means that there is no possible way of recovering the data.

This guide is DIME Analytics' step-by-step guide to encrypting data at all times in SurveyCTO and how to appropriately and securely handle the decryption keys.

Some of the steps in this guide can be implemented in more than one way.
To keep the guide simple, we will only mention one potential method for most steps.
Each time there are multiple ways we have chosen the one that,
based on our experience and testing,
is the simplest and least error-prone to implement.

## Prerequisites

These guidelines assumes that you:

1. Have a basic knowledge of SurveyCTO or ODK
1. Have access to a SurveyCTO server. You can set up a trial [here](https://login.surveycto.com/signup/step1.html).
1. Have SurveyCTO Desktop installed on your computer
1. Have a password manager that can handle secure notes ([our guidelines for setting up LastPass](https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/password-manager-guidelines.md))

## Topic 1 - Creating and properly storing a public/private key pair

For **encryption-at-rest** SurveyCTO uses [asymmetric encryption](https://dimewiki.worldbank.org/wiki/Encryption#Asymmetric_Encryption)
where there are two keys: one called the public key and the other called the private key.

In SurveyCTO, the public key is used at the point of data collection to encrypt your data as it is entered, 
and the private key is used at the point of downloading the data to decrypt your data. 
The server and the data entry teams will have the public key provided to them through the survey software automatically. 
The public key cannot decrypt the data.
Each public/private key pair is unique and no other private key can decrypt the data you encrypted with your public key.
You should never use the same key pair for two different projects,
but you do not need to create a new key pair for every form within a project.
We think that a good balance is to use one key pair for each project, and this practice typically conforms with IRB rules for regulating data access at the project level.


As the name suggests, it is essential to keep your private key secret. They key provides access to your encrypted data.
If you accidentally publish your private key or store it in an insecure location, then your data is no longer securely protected.
If you lose access to your private key, then there is no way to decrypt your data -- neither the software nor the service provider can restore it.
There is no security risk of accidentally publishing your public key.


### Step 1.1 - Creating a public/private key pair

You can create the public/private key pair on your SurveyCTO server.
Log in to your server, and navigate to the _Design_ tab. Then click _Tools_.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-create-1.png" width="75%"><!--- Image is read from master branch or use full URL-->

Then click _create a new key_ and then _Start key generator_

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-create-2.png" width="75%"><!--- Image is read from master branch or use full URL-->

You then download the keys in two files (one file for each key).
The name you enter in the next screen has no cryptographic function.
It will only be used to name the files that will be downloaded to your computer.
If you were to enter _name_of_my_project_ then your keys will be generated with these names:

* `name_of_my_project_Public.pem`
* `name_of_my_project_PRIVATEDONOTSHARE.pem`


You will store the keys in a password manager,
and then delete these files on your computer. 
Be sure to give the key files a name that you can recogize easily.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-create-3.png" width="75%"><!--- Image is read from master branch or use full URL-->

When you download the keys,
make sure that they are not downloaded to a folder that is synced to the cloud,
for example, Dropbox or OneDrive.
We do not want these keys to be sent to the cloud.
After storing these keys in a password manager,
delete these files from every local location they are saved in (such as the Downloads folder).
If they keys were already sent to the cloud,
then there is no way to fully delete them.


### Step 1.2 - Securely share and long term store the key pair

Saving the key pair in a regular folder on your computer is not a secure enough way of storing the key files.
Instead, our recommendation is that the key is stored in a password manager.
Make sure that you have a password manager set up and
that you are comfortable using it before proceeding with these instructions.
We will provide instructions for the password manager LastPass,
but this can be done in other password managers too.
A secure alternative to saving to storing the keys in a password manager
is to store the keys in an [encrypted folder](https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/veracrypt-guidelines.mdt)
on your computer,
but then you still need to store the key to the encrypted folder in a password manager.

Go to lastpass.com, log in to your vault and
click the plus sign in the red circle to create a new item.
Select _Secure Note_

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-store-1.png" width="50%"><!--- Image is read from master branch or use full URL-->

Then copy all the content of both keys you created and downloaded from your SurveyCTO server.
Make sure that you copy all content including the headers `-----BEGING PUBLIC KEY-----`. See example in the image below.

You should also make sure that you give a good name to your secure note with the keys.
This key is likely to be stored for years and
the name you give the key should make sense to you and to all other team members -
both current and future - in this project.

If you are using LastPass for many keys and passwords,
then it is good to organize all your secure items in folders.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-store-2.png" width="75%"><!--- Image is read from master branch or use full URL-->

### Step 1.3 - Delete the key files from your computers hard drive

A system of encryption is only as strong as its weakest link.
There is no point in storing the keys safely in a password manager,
if we also store them locally on our computers.
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

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-1.png" width="75%"><!--- Image is read from master branch or use full URL-->

Then give your new form a name and after turning on _Advanced Settings_. Then make sure that the checkbox "_Do you want this form's data to be encrypted?_" is checked. Click _Next_.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-a1.png" width="75%"><!--- Image is read from master branch or use full URL-->

Then select "_Paste public key text:_",
and then go to your secure note in your password manager and copy the public key.
Make sure that you only copy the public key,
and make sure that key header `-----BEGIN PUBLIC KEY-----`
and the key footer `-----END PUBLIC KEY-----` are included.
Then click _Next_ and then complete your form.
SurveyCTO will test that there are no errors in the public key,
but you should never start collecting data using an encrypted form before
you have followed our test instructions below.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-a2.png" width="75%"><!--- Image is read from master branch or use full URL-->

### Encryption method B - Excel sheet form definition

In your Excel file where you are developing your SurveyCTO form,
go to the _settings_ tab.
In the _settings_ tab there is a column called `public_key`.
Paste the value of the public key in the cell in the first row of that column.
In this method it is important that you do **not** include
the  key header `-----BEGIN PUBLIC KEY-----`
and the key footer `-----END PUBLIC KEY-----`. See example below.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-b1.png" width="25%"><!--- Image is read from master branch or use full URL-->

Go to the _Design_ tab in your SurveyCTO server. Click _Upload form definition_.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-encrypt-1.png" width="75%"><!--- Image is read from master branch or use full URL-->

Upload the form you with the public key included in the settings tab,
and then follow the instructions as normal.
SurveyCTO will test that there are no errors in the public key,
but you should never start collecting data using an encrypted form before
you have followed our test instructions below.

## Topic 3 - Publishable fields

One often overlooked feature when encrypting forms are publishable fields.
Publishable fields are fields for which
the collected data remain unencrypted even when the form is encrypted.
This data can be downloaded without providing the public key.

Here is one example where publishable fields can be useful.
Let's say you have hired a survey firm to collect data.
This survey firm wants to be able to download data from the SurveyCTO server to track progress,
but the IRB of your project does not allow you to share the respondents' data with the survey firm.
It is unlikely that the survey firm needs all data to track progress,
and often you do not need any respondent data other than respondent ID
and survey metadata such as consent, completion, revisit information, and so on.
In this case you decide together with the survey firm
on a minimal list of fields that they need to track progress.
If all of these variables are _not_ sensitive (which often is the case)
then you can make all of them publishable.
Then you can give the survey firm permission to download data from the server
or view it in the Data Explorer,
but as long as they do not have access to the private key,
they have no access to fields that are not made publishable.

To make a field publishable, you simply write "_yes_" in the _publishable_ column in the _survey_ tab in the questionnaire form.

To download the publishable data, go to the _Export_ tab in your SurveyCTO server.
Find your form and click "_Download for data_".
Then in the two sections as normal,
but in the "_Fields to include_" make sure that the checkbox
"_Publishable fields only (if you don't have the private key)_" is checked.
Then click _Download .csv now_.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-publish-1.png" width="75%"><!--- Image is read from master branch or use full URL-->

## Topic 4 - Using your private key to decrypt your data in SurveyCTO

Technically you can download encrypted data from your SurveyCTO server using a browser,
but then you first need to save your private key in a file on your computer.
In the workflow we recommend,
you avoid ever storing the private key in a file on your computer
after you have saved it in a password manager.
Instead, we recommend to only download data using [SurveyCTO Desktop](https://docs.surveycto.com/desktop/)
as you can copy your key from your password manager and paste it
without having to save it in a file first.

In SurveyCTO Desktop you log in to your server,
and click _Sync_ in the menu to the left.
Fill in the information as normal,
and in step 2 you need to paste the private key. See image below.
Go to your password manager and copy your private key.
Remember to include the header `-----BEGIN RSA PRIVATE KEY-----`
and the footer `-----END RSA PRIVATE KEY-----`.
Once you have copied it to your clipboard
(ctrl-C on Windows and command-C on Mac)
then simply click the _PASTE KEY_ button in SurveyCTO Desktop.
If the key you pasted is on the expected format,
then you will see a green checkmark
and the text "_Private key successfully pasted_".
However, SurveyCTO has not tested if you pasted the correct key,
it will only test that when you are actually downloading data.
If you have pasted the incorrect key, then you will get an error
and you will not be able to read the data.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-sync-1.png" width="75%"><!--- Image is read from master branch or use full URL-->

## Topic 5 - Testing your setup before

Testing your encryption and decryption workflow is easy
but we cannot stress enough how important it is that
you do indeed test the workflow before you start to collect real data.

The first thing you want to make sure that your form is indeed encrypted.
The easiest way to do that is to log in to your server and go to the _Design_ tab.
Find your survey and see if the icon for encryption is an open or closed padlock.
See the examples below where the form named _encrypted_form_ has a closed padlock
and the form named _unencrypted_form_ has an open padlock.
IF the padlock is closed then you know that all fields that
are **not** listed as publishable will be encrypted during data collection.

<img src="https://github.com/worldbank/dime-standards/blob/scto-guidelines/dime-research-standards/pillar-4-data-security/data-security-resources/img/scto-test-1.png" width="100%"><!--- Image is read from master branch or use full URL-->

However, there is a second thing you really want to test,
and that is to make sure you are able to decrypt the encrypted data.
To test your that you can decrypt data,
simply submit one test data submission,
then copy the private key from your password manager,
and use SurveyCTO Desktop to download your test submission.
If you are able to see the data that was collected in encrypted fields,
then you know that you will also be able to decrypt real data
once you starting to collect it.
