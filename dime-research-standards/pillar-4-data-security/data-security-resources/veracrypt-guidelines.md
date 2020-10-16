# DIME Analytics - Data Security Guides - VeraCrypt

[VeraCrypt](https://www.veracrypt.fr/) is a software used to implement [symmetric encryption](https://dimewiki.worldbank.org/wiki/Encryption#Symmetric_Encryption) in a way where you are in full control of who has access to the decryption key.

VeraCrypt is an open source software that is free of charge. While untested open source software may be risky to use, VeraCrypt is well-established open source software that has been reviewed by a large numbers of cybersecurity experts who use it themselves. It is widely accepted as your safest option.

## Guidelines for each part of a VeraCrypt workflow

These guidelines cover the following steps:

1. [Download and install VeraCrypt](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/veracrypt-guidelines.md#part-1-download-and-install-veracrypt)
1. [Set up a secure folder using VeraCrypt](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/veracrypt-guidelines.md#part-2-set-up-a-secure-folder-in-veracrypt)
1. [Encrypt files using the secure folder](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/veracrypt-guidelines.md#part-3-add-files-to-your-secure-folder)
1. [Access the encrypted files in the secure folder](https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/veracrypt-guidelines.md#part-4-access-encrypted-files)

### Part 1: Download and install VeraCrypt

VeraCrypt is the software that we recommend for use when encrypting data on your computer, regardless of whether it is in a non-shared folder or a shared folder like Dropbox. VeraCrypt is a free, open source software, so you can use it without having to pay for it.

The first time we use VeraCrypt we need to download and install the software. If you are using a World Bank desktop, then you must make an _eServices_ request and have an IT person installing the software for you.

If you are not using a World Bank computer, then you can download the software [here](https://www.veracrypt.fr/en/Downloads.html). For Mac computers there is only the _installer version_ option. Download that version. For Windows users there are four versions: choose the _installer_ version. After you have downloaded the installer file, open it and follow the instructions. Most people do not need to change any of the default values.

Anyone in your team that wants to access files you encrypt with VeraCrypt will also have to download the software to be able to decrypt and access those files.

### Part 2: Set up a secure folder in VeraCrypt

Before you can encrypt any files on your computer you must use VeraCrypt to create a special folder. In VeraCrypt this is called a "volume", but think of this as a secure folder that you can only access in a specific way using the software.

1. If you have VeraCrypt open, start by closing it, and re-open it. All our instructions will start from the opening page.

1. On the opening page click `Create Volume` (marked in red in the image below). Remember that _Volume_ in VeraCrypt means _secure folder_.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_1.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. In the _VeraCrypt Volume Creation Wizard_, you have three options. VeraCrypt has many advanced options, but for the type of work we do we will only use the default option, which also is the least complex. Make sure that _encrypted file container_ is selected and click `Next`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_2.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. In the next step, we will again choose the default option. So make sure _Standard VeraCrypt Volume_ is selected and then click `Next`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_3.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. Next you have to specify where you want to create the secure folder volume. The volume behaves as a folder where you can store files, but technically it is a file. In this aspect it is similar to a .zip-file which is a file that contains folder and files. You do not need to understand exactly how it works, but if you know how to use .zip files, you will be able to use secure folders. Choose a location and give the volume file a name. Click `select file`. Note that since a VeraCrypt volume is like any normal file, it can, for example, be moved, deleted, synced, e-mailed or transferred exactly like any other file.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_4.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. Select the desired path in the file selector. If you intend to share this folder, for example through Dropbox, then this should be inside your Dropbox folder (it can be moved there later in any case). If you are using the DIME Analytics folder setup then you should create this inside the "[encrypted folder](https://dimewiki.worldbank.org/wiki/DataWork_Folder#Survey_Encrypted_Data)". Then type the name of the secure folder in the _file name_ box (remember, the secure folder volume is actually a file). Then click `Save`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_5.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. Back in the _Volume Creation Wizard_ window, click `Next`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_6.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. Then you should select which encryption algorithm you want to use. Unless you know what you are doing and have a very specific requirement, always select AES (Advanced Encryption Standard).

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_6-a.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. One of the restrictions of VeraCrypt is that you need to decide what the maximum total size of the contents of the secure folder can be, before you put anything in it. Do not over-estimate too much, as the secure folder will always take up this much disk space, even when it is empty. If you realize in the future that the volume size was too small, then you will create a new, larger volume and move all the files there. You can also create another volume for different files. In this example, choose 250MB and then click `Next`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_7.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. In the next step, you need to create a secure password that you do not use for any other purpose. Secure passwords must only be shared using password managers, and password managers can also create strong unique passwords for you. Read VeraCrypt's instructions for what is a good password. After you have chosen your password and saved it to your password manager, copy it from your password manager to the first input field and then copy it to the second input field, and then click `Next`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_8.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. To make the encryption completely unpredictable, VeraCrypt uses your mouse movement to get a random input used when the folder is encrypted. This is nothing you need to remember, it just makes the encryption even harder to crack. Move your mouse inside the VeraCrypt window until the randomness indicator becomes green. The longer you move the mouse, the better. Then click `Format`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_install_9.png" width="50%"><!--- Image is read from master branch or use full URL-->

You have now created the secure folder. Go to the location where you created the folder to confirm it exists. It does not look like a folder, as it is technically a file. Double click on the folder to try and open it directly. Confirm that it doesn't open and you cannot do anything with it. Also see that the file is about 250MB big (or whatever value you chose) despite still being empty. The next part shows you how to use the secure folder.

### Part 3: Add files to your secure folder

In this part, we will learn how to use VeraCrypt to make the secure folder appear like a folder and not like an unreadable file, i.e. decrypting it. Decrypting a secure folder in VeraCrypt is called _mounting the volume_. The secure folder will never be exactly like a normal folder, but after mounting it you can access it the same way you usually access files by clicking on it or reading it directly from, for example, Stata. It will appear the same way on your computer like when you read files from a USB thumb drive.

A file encrypted in VeraCrypt is only decrypted while it is actively mounted. So if VeraCrypt were to stop working or if you turned of your computer or it would lose power, any mounted volume would immediately be un-mounted, and all files in it are immediately encrypted again. Try not to let this happen, however, as new changes you made or files you added since mounting it may not be saved correctly. Note that if you minimize VeraCrypt but do not fully close it your files will still be mounted.

You need to re-mount the secure folder after each time it was un-mounted, for example when you restart your computer. This is an important feature that makes your data secure. You should not keep _all_ your data files in the secure folder; you only need to encrypt the files with identifying or otherwise confidential data, so the process of mounting and re-mounting the secure folder should not be too burdensome since you don't work with this often.

1. If you have VeraCrypt open, start by closing it, and re-open it. All our instructions will start from the opening page.

1. First, you need to select a drive that will be used when you mount your secure folder. Even though the volume file you created in the last part might be stored on the `C:` drive, you need to select a different drive when mounting it. You can select any drive, but the examples in the rest of this exercise assume that you select `M:` as your drive. You can only select one encrypted file per drive, so if you were to decrypt several secure folders at the same time, you would have to select different drives for each of them.
    * MacOS users will note that the default file architecture is different from that of PC's. Mounted folders get placed under `/Volumes` regardless of the unmounted folder's location on your computer. We hope that Mac users can follow along these instructions despite them being written for Windows users.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_mount_1.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. Then click `Select File`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_mount_2.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. In the file selector, browse to the volume file that we created in the last part and select it. Then click `Open`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_mount_3.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. Back in the opening VeraCrypt window, click `Mount`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_mount_4.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. Go to your password manager and copy the password you created when you created the secure folder and then paste it here. Then click `OK`.

    <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_mount_5.png" width="50%"><!--- Image is read from master branch or use full URL-->

1. If the password is correct, you  have successfully mounted the container as a virtual disk `M:` (or whatever drive you chose).

1. Go to your file explorer and find the disk `M:`. Then open it to explore the content of the encrypted secure folder. This will now open an empty folder in your file explorer. This empty folder has the file path `M:`. This drive behaves very similarly to when you plug in a USB/flash drive to your computer and access files stored on that USB/flash drive.

1. Save some files in the empty folder. These could be any type of files, even though we will most often store data files in this folder.

1. You have now stored the files you added to the secure drive. However, as long as you have the secure folder mounted it can freely be accessed on the `M:` drive by anyone who has access to your computer. So go back to VeraCrypt, make sure that the mounted drive is highlighted and then click `Dismount`. Once you do that, then there is no way to access these files without the password you used when creating the secure folder volume, even if someone gets access to your computer or your hard drive.

### Part 4: Access encrypted files

In this part we will learn how to access the files in the secure folder. This is very similar to how we added files to the secure folder.

1. If you have VeraCrypt open, start by closing it, and re-open it. All our instructions will start from the opening page.

1. Mount the encrypted volume as described in Part 3 above. You can  select any drive when you mount the drive. However, you will soon learn that it will be easier to access the files from your code, if you are using the same drive for the same secure folder each time.

1. Double-click the mounted volume in the VeraCrypt window and see that the folder contains the folder you encrypted in the last part. If you were to access one of these files in Stata then you would use the file path `M:/name_of_file.dta` (if `M:` was the drive that you chose and `name_of_file.dta` was the name of your file.). Note that even though you created the secure folder volume file somewhere on the `C:` drive, the only way Stata can read it is through the mounted drive, `M:` in our examples.
    * MacOS users will note that the default file architecture is different from that of PC's. Mounted folders get placed under `/Volumes` regardless of the unmounted folder's location on your computer. Also, no matter which drive slot in VeraCrypt you mount the volume, the name of the mounted folder defaults to `NO NAME/`, resulting in the following default path to your file `/Volumes/NO NAME/name_of_file.dta`. In order to avoid duplicate file paths, MacOS users may want to change the name of the mounted volume, which will be preserved the next time it's mounted. The easiest way to do this is to slow double-click on the mounted volume's name on the desktop.

1. Once you are done working with the file containing confidential data that you keep in your secure folder, it is best practice to unmount it immediately in VeraCrypt. If you forget, the file will be unencrypted and accessible from anyone with access to your computer until you restart your computer.

## Note for sharing VeraCrypt folder on DropBox

VeraCrypt keeps the content in your encrypted folder very secure.
So secure that DropBox might have difficulties recognizing when
you make an edit to the content of your encrypted folder.
And this leads DropBox to not sync the new version of the folder,
as DropBox does not understand that there is a new version to sync.

This is what happens.
To make DropBox more efficient,
it does not look on each and every byte
of your files all the time to see if a file has changed.
That would take too much time and computational power
and DropBox would slow down your computer.
Instead it first looks at the time each file was last edited,
and checks if there are more recent files than the last synced file.
If DropBox notis that the last edit time is updated,
then it checks which bytes have been updated and sync those bytes.
However, DropBox cannot see the content of your encrypted folder,
it only sees the one file created in VeraCrypt.
VeraCrypt is all about privacy
and the default setting is therefore
to not reveal the last time any of
the content of your folder was edited unless you decrypt the content.
This way a hacker breaking in to your system
won't even know which is the most recent file you worked with.
However, this default setting makes collaboration
on encrypted folders over DropBox impossible.

This is how you solve this.
To change this default setting, open VeraCrypt,
in the top menu go to `Settings` -> `Preferences` and
then untick the option
"_Preserve modification timestamp on file containers_".
You need to restart VeraCrypt for the change to take effect.
See image below:

  <img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/vc_dropbox_setting.png" width="50%"><!--- Image is read from master branch or use full URL-->

## Practice exercise

This practice exercise can be done alone, but is better done with a second person. This exercise covers creating a secure folder with content, sharing it with someone, and securely providing them access to the content of the secure folder. The intention is that you both follow all steps so two folders are created and you share them with each other. If you do not have anyone you can do this exercise with, then you can simulate collaboration by sharing the encrypted folder to another computer where you open it. Or you can just wait until another day and try to access the folder after you've restarted your computer.

1. Create a Dropbox/Box/OneDrive folder that you share with the other person

1. Create one secure folder _each_ in this shared folder. Do not share the password with the person you paired up with yet. If both you and the person you paired up with have the same password manager, you should create long and strong password using that password manager and save the passwords there. If you do not have the same password manager, it is ok in this exercise to use a simple password. You should always use a password manager when you later securely share real data with your project team.

1. Look at your own and each other's file on the shared drive. *Important:* two separate people should not make changes to the contents of the same volume at the same time if it is stored on a sync service like Dropbox. So do not try to mount the other persons file until later in this exercise.

1. Mount your own secure folder in your computer and place some files in your secure folder in the shared Dropbox/Box/OneDrive folder.

1. While you both have your own secure folder mounted, does the file look different when you look at it in the shared folder? Can you tell if files were added or not? Can you tell if someone else has the file mounted?

1. Dismount your own drive and wait for the file to sync. Remember that it is bad practice to have two or more people have the secure folder mounted at the same time. Now share the password with the person you paired up with. How do you securely share a password?

1. Access your partner's encrypted file by mounting it on VeraCrypt using the password your partner shared with you. Can you see the files? Can you make edits to them?
