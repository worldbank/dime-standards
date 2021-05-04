# DIME Data Security Standards

Data security is important for two reasons:
**respecting the privacy of respondents or the terms of data licensing agreements** and
**making sure no one publishes papers using your data before you**.
To be fully compliant with the DIME Data Security Standards,
a project must follow all applicable items listed in the
[DIME Data Security Standards (detailed version)](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/dime-data-security-guidelines.md).

### DIME Data Non-Disclosure MOU

All Research Assistants and Field Coordinators at DIME must sign the
DIME Data Non-Disclosure Agreement (NDA)
as a condition of employment.
The NDA can be accessed [here](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/dime-data-nda.pdf)
but link will only work if you work at DIME.
You can email dimeanalytics@worldbank.org
if you want a copy of the NDA.

## DIME Data Security Resources

#### Secure back-ups of raw data in WB OneDrive

See
[DIME Data Back-up Guide ](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/onedrive-backup-guidelines.md)
for instructions on how all DIME projects should back up their data.

#### Encryption in transit

[Encryption in transit](https://dimewiki.worldbank.org/Encryption#Encryption_in_Transit)
keeps both your data and all the meta-data about your transfer
(your identity, your passwords etc.) safe.
If your URL starts with `http://` and not `https://`, **do not ever** send anything confidential to that website.
This includes research data, passwords, credit card details, or _any_ other information you would not post publicly on the internet.
Data and metadata transferred using `http` connections can be read by hackers,
and a hacker can pretend to be the website you think you are connecting to if you are using `http`.
While `http` is always insecure, you cannot always trust that `https` is secure.
Even when a page you visit uses `https`, some components on that page –
for example a form – could still use `http`.
Modern browsers are getting better at scanning all components of a website
to warn the user if any insecure connections are found.
Implementing `https` is not difficult,
so if you are suing well-established services like SurveyCTO, Survey Solutions, DropBox, etc.,
then you can simply trust that there are no insecure components
as long as the main URL starts with `https://`.

Similarly, if you are using an FTP connection to send data,
you should make sure that the URL you are connecting to starts with `ftps` and not `ftp`.

#### Encryption at rest

[Encryption at rest](https://dimewiki.worldbank.org/Encryption#Encryption_at_Rest)
and [encryption in transit](https://dimewiki.worldbank.org/Encryption#Encryption_in_Transit)
are not substitutes: they are complementary and both are necessary.
While encryption in transit protects both your data and your metadata (passwords etc.)
from anyone on the internet when data is sent to, from and between servers,
encryption at rest protects your data from the owners of those servers.

There are many ways to categorize different types of encryption
but a typical research user only needs to know about
[symmetric encryption](https://dimewiki.worldbank.org/Encryption#Symmetric_Encryption) and
[asymmetric encryption](https://dimewiki.worldbank.org/Encryption#Asymmetric_Encryption).
The only difference between these two that is relevant for researchers is
that symmetric encryption has one key, and that asymmetric encryption has two keys.
All keys should be stored in a [password manager](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/password-manager-guidelines.md).
Encryption at rest must be implemented in a way where no one
not listed on the IRB has access to decryption key(s).

Which type of encryption you should use depends on the context,
but unless you are using a service that requires asymmetric encryption,
you typically need symmetric encryption.
Use symmetric encryption to encrypt a file before you securely store,
send or share it with someone
if you want anyone with both the key and the encrypted file to be able to view and modify it.
We recommend a free, open-source software called VeraCrypt for manual symmetric encryption of files.
See the [DIME Analytics Guide to VeraCrypt](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/veracrypt-guidelines.md)
to encrypt files using symmetric encryption.
Symmetric encryption keys can never be shared as they both encrypt and decrypt the data.

Asymmetric encryption is best used when there is a one-way direction of the flow of data,
i.e. in data collection.
During data collection we want data to be encrypted on the tablet and sent to the server,
but we do not want each tablet to be able to download data from the server and decrypt it.
In this case, the data collection software is likely to have implemented everything for you,
so the only thing you need to do is keep track of the two keys, together called a public/private key pair,
using a [password manager](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/password-manager-guidelines.md).
The public key (which encrypts the data) can be shared publicly but the private key (which decrypts the data) cannot.
See [DIME Analytics Guide to Encryption in SurveyCTO](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/surveycto-encryption-guidelines.md).

#### De-identification

To make encryption less disruptive in a research team's workflow,
we recommend that all teams remove personally-identifying information (PII) from their data
at the earliest possible opportunity.
The resulting de-identified datasets do not need to be encrypted
and therefore can be used on a day-to-day basis
without the need to manually encrypt and decrypt the data.
Read [DIME Analytics Guide to De-identification](https://dimewiki.worldbank.org/wiki/De-identification) for more details.
Remember to save a backup copy of the original identified data in a non-shared, non-synced OneDrive folder.

#### Password management

The only safe way to share keys and passwords is to use password managers.
and password managers are great at making it easy to follow password best practices.
You only need to come up with and memorize one very strong password – your _master password_, used to log in to the password manager account.
To make sure that you have a very secure master password, see the
[DIME Analytics Guide to Secure, Memorizable, and Long Passwords](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/memorizable-strong-password-guidelines.md).
Once you have a memorizable and sufficiently long password,
you should follow the [DIME Analytics Guide to Password Managers](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/password-manager-guidelines.md).

#### Secure, memorizable, and long passwords

While you should use a password manager to create extremely secure passwords for almost all passwords you use,
there are some cases where it is not possible to use the password manager.
One examples is the master password you use to access the password manager itself.
Another example is your computer logon password,
as you cannot access your password manager until you have started your device.
To create a secure password you can memorize,
see the
[DIME Analytics Guide to Secure, Memorizable, and Long Passwords](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/memorizable-strong-password-guidelines.md).
