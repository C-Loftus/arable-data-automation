from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import serialNums

def uploadFile(fileToUpload):
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

    folderName = serialNums.private.returnFolderName() # Please set the folder name.

    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            file2 = drive.CreateFile({'parents': [{'id': folder['id']}]})
            file2.SetContentFile(fileToUpload)
            file2.Upload()


if __name__ == "__main__":
    testInput = input("Give your file name : ")
    uploadFile(testInput)