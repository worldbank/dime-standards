# DIME Analytics Data Security Policy Details

All confidential data used by DIME must be handled in such a way that
there is no risk that anyone who is not on the IRB for the specific project has any ability to access the data.

Data can be confidential for multiple reasons, but the most common reason is that it contains
[personally identifiable information (PII)](https://dimewiki.worldbank.org/De-identification#Personally_Identifiable_Information).
Other reasons include that the data has been shared with you under a data usage license
that requires that the data is kept confidential.

## Transferring and sharing confidential data

All data transferred over the internet must be [encrypted in transit](https://dimewiki.worldbank.org/Encryption#Encryption_in_Transit).
This prevents people from intercepting and reading your data.
* Encryption in transit is required even if you encrypt the data before transferring it,
as it is the only way to protect the metadata of your transfer,
such as passwords and tokens, IP addresses, and other private information.
* You rarely have to worry about encryption in transit,
as all well-established services that send data and files do this
without any required action from the user. This includes SurveyCTO,
Survey Solutions, OneDrive, Dropbox, etc.
* If you are using another service where you are not sure whether encryption in transit is implemented,
confirm with DIME Analytics before using it.
* Email is never a secure option for confidential data as there is no way to enable complete encryption in transit.

All data stored on servers must be [encrypted at rest](https://dimewiki.worldbank.org/Encryption#Encryption_at_Rest).
It must be encrypted **before** it is sent to the server
and remain encrypted as long as it is stored on the server.
This prevents people who can access that server from taking and reading your data.

* Even though SurveyCTO, Survey Solutions, Dropbox, and other services provide
[encryption in transit](https://dimewiki.worldbank.org/Encryption#Encryption_in_Transit),
the data is often _also_ stored on their servers (no matter how briefly)
before any intended recipient can access that data.
Since those companies are administrators on their own servers,
they can read your data if it is not additionally encrypted by _you_ before it even reaches their servers.
* Encryption is implemented in World Bank OneDrive on World Bank devices
to use World Bank logins and passwords to automatically encrypt all data on-the-fly.
This is why World Bank OneDrive is the rare exception where we can store confidential data
without manually encrypting it and it is still properly encrypted.
The same is _never_ true for non-enterprise versions of OneDrive.
* For all other data transfer and storage services we must manually encrypt the data.
The data needs to be encrypted before being sent to any server in such a way
where no one who is not listed on the IRB has access to the decryption key.
This is typically done differently depending on whether it is a one-way transfer (data collection)
or two-way transfer (data sharing):
  * _One-way transfer_: Most data collection services, including SurveyCTO and Survey Solutions,
  have implemented [asymmetric encryption](https://dimewiki.worldbank.org/Encryption#Asymmetric_Encryption)
  using [private/public key pairs](https://dimewiki.worldbank.org/Encryption#Public.2FPrivate_Key_Pair).
  This means data encryption is handled automatically once enabled,
  but decryption still requires you to manually decrypt the data using the decryption key.
  The public key is stored on the server and on the tablets,
  but only people listed on the IRB may have access to the private key that can decrypt the data.
  The private key needs to be stored and shared using a
  [password manager](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/password-manager-guidelines.md).
  * _Two-way transfer_: On most other services, for example Dropbox, non-WB OneDrive, email, WhatsApp, and SMS text messages,
  among many other insecure modes of communication, we have to implement
  [symmetric encryption](https://dimewiki.worldbank.org/Encryption#Symmetric_Encryption) ourselves.
  This means that only already-encrypted data may be shared using that service, and the key is shared separately inside a
  [password manager](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/password-manager-guidelines.md).
  Under symmetric encryption, the data is encrypted and decrypted manually using the same key.
  The key may only be shared with people listed on the IRB who need access to the raw data.
* Confidential data that is properly encrypted at rest can sometimes be securely viewed by users through the browser.
For example, a shared WB OneDrive folder can be viewed in the browser,
and SurveyCTO data can be viewed in their Data Explorer after providing the private key.
When that data is downloaded using the browser it is no longer encrypted
and needs to be encrypted as it is saved to the local computer.

## Storing confidential data

PIs should save a copy of the unaltered raw data in a WB OneDrive folder as backup.
* This folder should not be synced to any computer, and it should not be shared with anyone, so it remains completely under individual control.
* If there are multiple PIs on a project,
each of them can save a backup of the data _separately_ for added layers of security.
* The enterprise-grade WB OneDrive is automatically encrypted, so no extra layer of manual encryption is required,
and therefore there is no risk of data loss due to lost decryption keys.

Any folder or file on your computer containing confidential data must be encrypted,
regardless of whether it is shared or not. See the DIME Wiki entry for
[encrypted folders](https://dimewiki.worldbank.org/Data_Security#Locally_storing_identified_PII_data) for more details.
* You must always keep confidential data encrypted and decrypt it each time you use it,
regardless of how frequently you need to access it.
* If your analysis does not rely on the confidential part of the data,
then the confidential part of data can be removed from the data set as soon as possible
and you can keep an unencrypted copy of the remaining data on your computer.
Once this is done you can even share it unencrypted on insecure services like Dropbox.
  * For  [PII](https://dimewiki.worldbank.org/wiki/Personally_Identifiable_Information_(PII))
  data this process is called [de-identification](https://dimewiki.worldbank.org/De-identification).
  Identifying and removing direct identifiers (names, national IDs, phone numbers, etc.)
  is usually straightforward and easy. However, it is more challenging to identify _indirect_ identifiers, or
  information that in combination with other information is identifying,
  for example village plus date of birth, or age plus profession.
* The [`iefolder`](https://dimewiki.worldbank.org/Iefolder) structure has a dedicated folder called
[`EncryptedData`](https://dimewiki.worldbank.org/DataWork_Folder#EncryptedData)
has been created for this purpose.
If any confidential data is stored on your local computer,
then that should be stored in that folder to make it easy to keep track of what needs to be encrypted or not.
Note that `iefolder` does not encrypt the folder. You still have to do so manually using a
[symmetric encryption](https://dimewiki.worldbank.org/Encryption#Symmetric_Encryption) tool, and share the key using a
[password manager](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/password-manager-guidelines.md).
