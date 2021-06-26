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

    folderName = serialNums.private.returnFolderName() # set the folder name.

    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()



    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for tempFile in file_list:
        if tempFile['parents'] == [{"kind": "drive#parentReference", "id": serialNums.private.driveBackupFolderNumber()}]:
            tempid = tempFile['id']
            temp = drive.CreateFile({'id': tempid})
            temp['parents'] = [{"kind": "drive#parentReference", "id": serialNums.private.driveBackupFolderNumber()}]
            temp.Upload()


    for folder in folders:
        if folder['title'] == folderName:
            file2 = drive.CreateFile({'parents': [{'id': folder['id']}]})
            file2.SetContentFile(fileToUpload)
            file2.Upload()




if __name__ == "__main__":
    testInput = input("Give your file name : ")
    uploadFile(testInput)
