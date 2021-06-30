from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import serialNums
import json

def uploadFile(fileToUpload):
    ### Setup Authentications
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("conf/mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("conf/mycreds.txt")
    drive = GoogleDrive(gauth)

    ### Get the folderID
    folderName = serialNums.private.returnFolderName() # set the folder name.
    folderId = None
    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            folderId = folder['id']

    ### Move all old files to the backup directory
    allFiles = drive.ListFile({'q': "'" + folderId + "' in parents and trashed=false"}).GetList()
    for file in allFiles:
        file2 = drive.CreateFile({'id': file['id']})
        print(file2['title'])
        file2['parents'] = [{"kind": "drive#parentReference", "id": serialNums.private.driveBackupFolderNumber()}]
        try:
            file2.Upload()
        except:
            pass

    ### Upload the file that was passed in
    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            file2 = drive.CreateFile({'parents': [{'id': folder['id']}]})
            file2.SetContentFile(fileToUpload)
            file2.Upload()

def downloadFile():
    ### Setup Client Authentication
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("conf/mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("conf/mycreds.txt")
    drive = GoogleDrive(gauth)

    ### Get folder name
    folderName = serialNums.private.returnFolderName() # set the folder name.
    folderId = None
    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            folderId = folder['id']


    ### Download all files in the folder and return the amount downloaded 
    ##### The function that calls this one will need to handle the case in which 
    ##### multiple files are downloaded. May not be desirable.
    allFiles = drive.ListFile({'q': "'" + folderId + "' in parents and trashed=false"}).GetList()
    filesDownloaded = 0
    for file in allFiles:
        file2 = drive.CreateFile({'id': file['id']})
        file2['parents'] = [{"kind": "drive#parentReference", "id": serialNums.private.driveBackupFolderNumber()}]
        try:
            file2.GetContentFile("csv/eere")
            filesDownloaded += 1
        except:
            # it was a folder if it fails, which is fine so just pass without doing anything
            print("Failure downloading contents from file named: '", file2["title"], "'If it is a directory, ignore this error. \
                PyDrive only downloads files, not directories, so this is to be expected.")
    return filesDownloaded
        

if __name__ == "__main__":
    testInput = input("Give your file name : ")
    uploadFile(testInput)
