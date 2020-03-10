# DIME Analytics - Data Security Guides - Password managers

**Weak passwords** is one of the two main causes of data breaches.
(The other one being outdated software, so always update your software when prompted to)

**Strong passwords** should be very long and different from other passwords you use.
Password that protects confidential data should be at least 15 characters long
(preferably more than 30 if allowed) and consist of completely random numbers, letters and symbols.
For example, `mPFaAse&9x^R9vxg2*8ZA2BFik#KyXuj`. No one can memorize such passwords by heart,
but password managers makes it easy to create, securely store and work with such passwords.

## Password managers make it easy to use super-strong passwords

With password managers you only need to remember one password, called the _master password_.
The master password is used to unlock the password vault in your password manager.
All other passwords should be long random strings and your password manager will store
and give you access to them through the password vault.

A properly implemented password manager does not treat your _master password_ like regular websites treat a password.
Passwords on sites like facebook.com, dropbox.com etc. are sent to their web servers
when you access your profile in their data bases to verify that you are you.
In a properly implemented password manager however,
the password vault is sent encrypted to your browser,
where your master password then is used to decrypt it.
This way your master password never travels on the internet, which is much more secure.

### The two password managers we recommend

This guide recommends two password managers, [LastPass](https://www.lastpass.com)
and [Bitwarden](https://bitwarden.com). LastPass is a closed-source
but widely used password managers that anyone with a worldbank.org email can get a 1 year premium trial access.
LastPass's browser extension is also approved for World Bank devices.
Since LastPass is a closed-source software
(meaning that no one from the outside can confirm that it is properly implemented)
we also want to recommend the open-source alternative Bitwarden
(recommended for example [here](https://www.privacytools.io/software/passwords)).
Bitwarden has been scrutinized by hundreds of independent cyber security experts that have no profit incentive to not disclose weaknesses.
Bitwarden can still be used on World Bank devices, but its browsers extension cannot be installed.

### The most secure types of password managers

This guide recommends [LastPass](https://www.lastpass.com) and [Bitwarden](https://bitwarden.com)
which are both cloud based password managers,
but the most secure type of password managers does not store your password vault in the cloud.
However, password managers that do not store the password vault in the cloud are much less user-friendly,
as you need to manually sync password across devices, and if you do not carry your device with you,
then you have no way to access any of your passwords.
Cloud based password managers are still extremely secure as long as they are implemented correctly,
but for the sake of completeness, we want to mention that there are doubly-extremely secure non-cloud password managers like [KeePassXC](https://keepassxc.org).

## Creating you master password

Your master password should be the only password you should have to remember by heart,
in addition to your computer log-on.
You will not be able to use your password manager before you are logged in to your computer,
which is why you also need to memorize your computer log-on password.

Since these passwords authorize access to so much else, they also need to be very secure.
They will never be as secure as `mPFaAse&9x^R9vxg2*8ZA2BFik#KyXuj`, but
[DIME Analytics guide to memorizable secure passwords](https://github.com/worldank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/memorizable-strong-password-guidelines.md)
helps you create as secure as possible "memorize-able" passwords.

# LastPass - Guidelines

If you work for the World Bank you can get a 1 year free LastPass premium trial.
The only aspect in which a premium account differs from a free account
that is relevant to a typical researcher
is how many people each secure item (password, key-file etc.) can be shared with.
When you create a password on LastPass, you are the owner of that item.
An owner using the free LastPass account can only share that item with one person,
but someone using LastPass premium can share it with any number of people.
See a complete list of the differences between free, premium, family, and business
 accounts [here](https://www.lastpass.com/plans).

## Create LastPass account

Before you set up your LastPass account, use the
[DIME Analytics guide to memorizable secure passwords](https://github.com/worldank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/memorizable-strong-password-guidelines.md)
to create a very secure memorizable master password regardless of which instruction on how to sign up you are using below.

_World Bank:_ If you have a worldbank.org email address and want access to the 1-year free trial of LastPass premium you should follow
[these instructions](https://worldbankgroup.sharepoint.com/sites/ITS/cybersecurity-blog/Pages/Last-Pass-03062019-161721.aspx?deliveryName=DM10667&deliveryName=DM44419)
(only available if you have access to the WB's intranet).
This document also covers how to install the browser extension in your browser.

If you have a worldbank.org email address, but you already have a LastPass using another email address,
then you can upgrade your current account using the same instructions as above.

_Non-World Bank:_ Create a free LastPass account [here](https://lastpass.com/create-account.php) here.
If you already know that you want to pay for a premium account,
you should still start with creating a free account and then upgrade it.

### Install LastPass' browser extension

All popular password managers offers browser extensions that make it easy to copy passwords
from your password vault to a field in the browser where you need them.
You do not need to install the browser extension
(you are giving LastPass a lot of access to your data by doing so), but most people do.
If you do not install your browser extension,
you will have to go to lastpass.com each time you need any password from your password vault.

Regardless of using a World Bank device or not,
go to https://lastpass.com/misc_download2.php, click the `Quick install` button at top of the page,
and follow all the instructions.

## Edit LastPass' insecure default settings

One reason many cyber-security forums recommend _against_ using LastPass is that there are a lot of options that make it less secure.
This section will walk you through settings you change for LastPass to be safer.
The IT department at the World Bank has approved LastPass but it also created a
[guide for how to make LastPass safer](https://worldbankgroup.sharepoint.com/sites/ITS/cybersecurity-blog/Documents/LastPass/LassPass%20Security%20Guidelines.pdf)
(only available if you have access to the WB's intranet).

We know that most of you will just skip this and go with the default settings,
but you should really follow the **Extension login** window and **Extension logout** advice.

### Extension login window

If you installed the browser extension, the first thing you need to do is to log in.
You will see the menu shown in the picture below.
It is perfectly fine to tick the box `Remember Email` but **never ever** tick the `Remember Password` button.
The fact that LastPass even offer that option should make you cringe.

Similarly, you should **never ever** let your browser save your LastPass master password.
You really need to meorize it and type it each time you need access to your vault. This is the only secure way.

<img src="https://github.com/worldank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-ext-login.png" width="25%"><!--- Image is read from master branch or use full URL-->

### Extension logout

After never saving your password in your browser extension login,
the second most important setting to change is enabling automated log out.
The default behavior is that you are never logged out automatically,
unless you log out manually or turn off your computer. That is really insecure.

In each browser you installed the extension, go to _account options_ in the browsers extensions and click extension preferences.
In the `General` tab, make sure that both the option "_Log out when all browsers are closed_"
and "_Log out after this many minutes of inactivity_", and add a number of minutes.
We recommend 5 but anything up to 15 minutes is ok.
(If you installed the client instead of the browser extension, you will have to take similar action there.)

<img src="https://github.com/worldank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-ext-logout.png" width="75%"><!--- Image is read from master branch or use full URL-->

### Master Password Recovery

Any service that offers any kind of password recovery is always exposed to some level of insecurity.
In LastPass password recovery is enabled by default but we recommend that you disable it.
**Important note:** The flip side of the increased security of no recovery option is that if you forget your master password,
it is completely impossible for you to get access to your account ever again.

Instead, we recommend LastPass'
[Emergency Access feature](https://support.logmeininc.com/lastpass/help/set-up-and-manage-emergency-access-lp030013)
where you grant one other LastPass user that you trust (ex. a family member)
a time-delayed one-time access to all your passwords that they can export and give to you.
If you really trust that person, then this is a safe option.
There is no way this give you access back to your account,
but you can start a new identical account by importing the information your trusted person exported for you.

To disable the default master password recovery you must -
in each browser you installed the extension - go to _account options_ in the browsers extensions
and click extension preferences. Under the `Advanced` tab you should untick the option
"_Save a disabled one-time password locally for account recovery_" highlighted with a yellow circle in the image below. (If you installed the client instead of the browser extension you will have to take similar action there.)

<img src="https://github.com/worldank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-optrecovery.png" width="50%"><!--- Image is read from master branch or use full URL-->

If you want keep account recovery for any reason, we strongly recommend that you enable SMS Account recovery.
The default behavior is that LastPass sends you an email when you request account recovery.
If a hacker has gained access to your computer,
then it is likely that they have access to both your email and your browser extension
and can gain access to all your passwords by requesting an account recovery.
Setting up SMS Account Recovery means that an SMS is sent instead,
which is safer since it is less likely someone that has access to your phone and
your computer at the same time. However, if you have the app installed on your phone,
someone can get access to both the app and SMS by hacking your phone.
There is always some insecurity associated with enabling master password recovery.

To enable SMS recovery, go to your password vault and click account settings.
In the general tab you find the button in the image below. Click `Update Phone` and follow the instructions.

<img src="https://github.com/worldank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-smsrecovery.png" width="50%"><!--- Image is read from master branch or use full URL-->

## Use LastPass to create and store a super-strong password

After you have gone over your account settings you can start using LastPass to
create and store super-strong password like `mPFaAse&9x^R9vxg2*8ZA2BFik#KyXuj`.
In this tutorial we will create secure notes in which we can save passwords or encryption keys.
There is a specific item for passwords in LastPass,
but a secure note can also store instructions for current and future team members
on how to use the password or key. If you want to use LastPass to secure your personal online accounts,
then you should use passwords instead of notes.

To create a new secure note, open up your LastPass vault.
You can either do this in your browser extension or by going to lastpass.com and log in.
When you are in your vault, select `Notes` in the left menu
and then click the plus sign in the large red circle in the bottom right corner.

<img src="https://github.com/worldank/dime-standards/blob/bootcamp-material/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-create-1.png" width="75%"><!--- Image is read from master branch or use full URL-->

Then you need to create a long random string that can be used as password or key.
You can click the browser extension icon, and then select `Generate Secure Password`.
If you do not have the browser extension installed, you can instead go to https://www.lastpass.com/password-generator.
There you will have the same options but it will look slightly different.

<img src="https://github.com/worldank/dime-standards/blob/bootcamp-material/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-create-2.png" width="30%"><!--- Image is read from master branch or use full URL-->

When you create your password, you should create a very long password.
32 is a common maximum length. Some services will not allow such long passwords,
and then you should use the maximum length allowed.
You can choose a password that is even longer than 32, that makes it safer,
but already 32 is practically impossible to crack.

Since you will be storing this password in LastPass,
you will not need to memorize this password and there is no point of making it
"_Easy to say_" or "_Easy to read_". If you select "_All characters_",
then the password is a completely random string
which is the most difficult password for a hacker to crack.
It is safest to have a password that consists of all four
"_Uppercase_", "_Lowercase_", "_Numbers_" and "_Symbols_".
Some services do not allow all types of symbols in their password,
and then you can just untick "_Symbols_"
as passwords of length 32 are still very secure even without them.
Finally, click the copy symbol to the right of the password to copy the password to your clipboard.

Remember that you should **always** create a new password for each service,
or for each encryption key that you set up.
One of the most important password safety aspects of a password manager
is that it allows you to have _different_ super strong password on each site.

<img src="https://github.com/worldank/dime-standards/blob/bootcamp-material/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-create-3.png" width="30%"><!--- Image is read from master branch or use full URL-->

It is **very important** that you do not use the password you just created
before you have successfully stored it in your LastPass vault.
Instead, immediately after you have copied your new password,
close the password generator and go back to the secure note you are creating.
Paste the new password in the secure note,
and then write a short description of what you will be using this password for.
Anything you write inside this note is secure as well,
so you are safe to write exactly what this key is used for
and any other instructions you only want to share with people that has access to this key.
When you are done, click `Save`.

<img src="https://github.com/worldank/dime-standards/blob/bootcamp-material/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-create-4.png" width="80%"><!--- Image is read from master branch or use full URL-->

If you are new to LastPass you should make sure this secure note is successfully saved
by logging out of your account, and then log in again.
If you see the secure note and the password in it after you have logged in again,
then you know that this password is secured in LastPass and
can only disappear if you delete it or lose access to your LastPass account.

You can now use your super strong password, for example as a key in
[VeraCrypt](https://github.com/worldank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/veracrypt-guidelines.md).
See next session for how to share it.

### Use LastPass to securely share a password

An important feature of LastPass is that you can securely share items you have stored in your vault with other accounts.
For this to be secure, you can only share these items with other accounts on LastPass,
so anyone you want to share this item with needs to create their own account on LastPass.

To share an item that you have already saved to your vault,
hold your mouse over the item you want to share and click the people symbol
(see red circle in the image below).

<img src="https://github.com/worldank/dime-standards/blob/bootcamp-material/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-share-1.png" width="50%"><!--- Image is read from master branch or use full URL-->

Then you simply add the email address associated with the account you want to share the secure item with.
If you share the item with an email the other person did not use when signing up for LastPass,
then the invitation link will still be sent to the email you used.
However, when they click the link they will be asked to sign in,
and when they sign in to another account they will not have access to the item you shared.
You will then see the invitation as pending until that person has successfully accepted it.

<img src="https://github.com/worldank/dime-standards/blob/bootcamp-material/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-share-2.png" width="40%"><!--- Image is read from master branch or use full URL-->

### Some remarks on shared items

If you create an item then you are the owner of that item, even if you share it.
There are several differences to what you can do to an item
depending on whether you are the owner of it or it was shared with you.
Some of those differences are listed below.

LastPass occasionally changes how secure items are handled and
tends to not inform their users when changes are made.
While DIME Analytics will update this page if we notice changes,
we cannot guarantee that any of these remarks are up to date.

#### Forwarding secure items

If an owner shares an item with someone, then that someone cannot forward the item to other LastPass accounts.
Only the owner can share an item.
However, you have no control over what the person you share a secure item with does with that information.
They can copy it to their computer, or copy it to a new secure item that they share.

#### Owner revokes access

If an owner shares an item with someone, then the owner can revoke that access,
and the next time that someone logs into LastPass they will not see the item.
The revoking is not instant, so if that someone has their vault open,
they will have access to the item until they log out from their vault or refreshes the page.
And remember that LastPass' default setting is to never log out.

Another important remark about revoking access is that you cannot know if the other pesron
copied it to another secure note that they own or saved it somewhere else.
The only way you can be really sure that a person does no longer have access to a resource
is to revoke access and then change the password.

#### Owner deletes and item

If an owner deletes an item it will be gone for everyone and there is no way to recover that secure item.
Similarly to revoking access to an item, this is not instant,
and other users have access to the item if they were already logged in
until they log out from their password vaults or refresh the page.

#### Someone deletes an items

If an owner shares an item with someone, and that someone accepts the invitation, then
they can then delete the item in their vault. They will loose access to the item,
but nothing happens to the item in the owners password vault.

#### Owner updates the item after sharing it

If an owner shares an item with someone, and after that someone accepts the invitation,
the owner updates the information,
then that is reflected next time the other person refreshes their vault.
Only the owner can modify a secure item.

## Securely save public/private key files using LastPass

Unless you actively choose another installation option,
then the basic version of LastPass cannot save files in the vault.
Public/private key pairs are often generated as files (often two files with one key in each file).
One way to store them in LastPass is to install the advanced version of the LastPass extension,
but then you need to make sure that anyone else you are sharing this file pair with also does that.
Another issue with this is that the only way to access the content of those files
is to download them to your computer each time you are using them.
This in itself is a security weakness as you must always remember to delete the file from your computer.

Instead, we recommend that you copy the content of these files and save them as a secure note in LastPass.
The content of public/private key files are just long strings,
which we can save in secure notes, and we have already learned how to do that.
Most services that use public/private keypairs allow you to copy the key string
and paste it in a field instead of uploading a file.
This means that we can copy it directly from our LastPass vaults
and thereby never save the files on our computers.

See the image below how you can store a key in a secure note.
This key comes from SurveyCTO and the keys they generate start with something like
`-----BEGIN PUBLIC KEY-----` but the key pair you use might not have something like that.
It is still a good idea to include a header like this in your secure note,
so that you or anyone you shared this item with remember which key is which,
where it starts and ends, etc.

<img src="https://github.com/worldank/dime-standards/blob/bootcamp-material/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-store-keypair.png" width="80%"><!--- Image is read from master branch or use full URL-->

## Your passwords are version controlled

Another feature of LastPass that is important to know is that it version controls all your edits to secure items.
This has two consequences that you should be aware of.
First, let's say you have a secure note where you have several bullet points of sensitive information.
Then you delete all but one bullet points, and thereafter share it with someone.
That someone can use the version control to access all original bullet points.
So all previous versions of a secure item is available to everyone that has access to the secure item.

Second, if you accidentally modified information in your secure item then you can restore it
as long as you did not delete the whole item.
For example, let's say you are using the private key to download data and
you cut-and-paste the key instead of copy-and-paste and save it.
Your secure note would then look like the image below.

<img src="https://github.com/worldank/dime-standards/blob/bootcamp-material/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-versioncontrol-1.png" width="80%"><!--- Image is read from master branch or use full URL-->

In the image above, you see the version control button highlighted with a red circle.
If you click that button you will get to a menu where you can see all version of this secure item,
and can copy any value and then close the version window and paste it back into the secure note.

<img src="https://github.com/worldank/dime-standards/blob/bootcamp-material/dime-research-standards/pillar-4-data-security/data-security-resources/img/pw-lp-versioncontrol-2.png" width="80%"><!--- Image is read from master branch or use full URL-->
