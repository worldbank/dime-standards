# DIME Analytics - Data Security Guides - WB OneDrive Back-up

This guide is for the World Bank's Enterprise version of OneDrive (WB OneDrive),
and not all parts of this guide should be followed using regular OneDrive, DropBox or any other syncing service.
The non WB OneDrive sync services are not secure enough for us to recommend for uploading identified data
without manually encrypting it first.

A folder created in WB OneDrive cannot be synced to a non-World Bank device
even if owner of that device has been invited to the folder.
This is because it is installed with extra layers of encryption that is connected to our WB computer log-ons.
While that makes it an unsuitable tool for day-to-day collaboration with team members that do not have a World Bank computer
(as they cannot sync the folder),
it makes it an excellent tool for back-ups of raw data,
where there is no risk of losing data as a result of loss of encryption keys.

While a person without access to a World Bank computer cannot sync a WB OneDrive folder, 
they can still follow all the steps in this guideline to set up a WB OneDrive back-up folder using the browser. 
Just make sure that you log in to WB OneDrive and not regular OneDrive. 
Here are two ways to make sure it is WB OneDrive:
* After you log in yto your WB OneDrive account, make sure that the URL has re-directed to `worldbankgroup-my.sharepoint.com` or something like that
* Check the account you are logged in with in the top right corner. Make sure this uses your worldbank.org email

## WB OneDrive back-up folders

While an easy process, setting up a back-up folder in WB OneDrive is an extremely important process. 
The only way the back-up folder should differ from most WB OneDrive folders is that this folder should not be synced to any device,
and it should not be shared with anyone.

You are allowed to sync identified data in WB OneDrive folders to your device,
but since that there is a risk that you by accident delete a folder on your computer,
you should not sync the back-up folder.
If you want the data synced to your computer,
create another folder that is not your back-up folder and sync that folder instead.

You are allowed to share identified data with other World Bank members using WB OneDrive,
but since there is a risk that they by accident, or because they did not know it was a back-up folder,
delete your back-up folder, you should not share your back-up folder.
Again, if you want to use WB OneDrive to share the data, create another folder and share that folder.
If you are more than one PI in a project, then each PI can create their own WB OneDrive back-up folder.

## Steps to set up a WB OneDrive back-up folder

Go to [WB OneDrive](http://onedrive.worldbank.org) and create a new folder.
We recommend that you create one top back-up folder in which you create a sub-folder for each project.
Then you will not lose track of your back-up folders.
We call our folder `backup-data` but you can name it whatever you want
to make sure you never confuse this folder for another folder.
To create a folder, click `+New` and then `Folder` and follow the instructions.

<img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/onedrive-backup-1.png" width="75%"><!--- Image is read from master branch or use full URL-->

In the top back-up folder, create one folder for each project you want to back up
by clicking `+New` and then `Folder` again.

<img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/onedrive-backup-2.png" width="75%"><!--- Image is read from master branch or use full URL-->

In each project folder, create one folder for each data source you want to back up,
by clicking `+New` and then `Folder` again.
A data source can be a survey round (baseline, endline etc.),
admin data (data shared with us from government counter parts) etc.
The main difference between data sources relevant to back-ups are if they are
continuous (meaning we keep getting new data) or
discrete (meaning that once we have the data set it will not be updated again).

An example of a discrete source of data is a typical survey round.
Once we are done collecting data we will not get more data for that survey round.
That data should be backed up in WB OneDrive after the data collection is completed
but before the data collection server is closed down.
For continuous data sources there is no equally obvious point when the data should be backed up,
but it should be often enough that a potential loss of data between back-ups
is not too devastating for the project.

<img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/onedrive-backup-3.png" width="75%"><!--- Image is read from master branch or use full URL-->

Once you have created the folder for your data source,
simply drag all the files you want to back up here.
You can drag a whole folder and all its content at the same time.
You should back up the most raw version of your data, even if that is a bunch of csv files.
Since storage space will not be an issue as you will not sync this folder,
you can back up both, the rawest files and a data set created from the raw files.
Even if these files are identifying you do not need to manually encrypt them before uploading them.

<img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/onedrive-backup-4.png" width="75%"><!--- Image is read from master branch or use full URL-->

You will see the file in your back-up folder once it is done uploading.
If you want to upload more files you just keep dragging them there.
Then you are done and your files are securely backed up.
Close your browser and do not navigate to this folder more than necessary
to minimize the risk that you delete a file by mistake.

<img src="https://github.com/worldbank/dime-standards/blob/master/dime-research-standards/pillar-4-data-security/data-security-resources/img/onedrive-backup-5.png" width="75%"><!--- Image is read from master branch or use full URL-->
