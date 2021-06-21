from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import ApiRequestError
import sys
from datetime import date
from yaml.events import DocumentStartEvent

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
    file1 = drive.CreateFile({'title': str(date.today()) + fileToUpload})
    file1.SetContentFile(fileToUpload)
    try:
        file1.Upload() # Files.insert()
    except ApiRequestError:
        sys.exit("Error uploading file due to an API issue. Try again")

if __name__ == "__main__":
    testInput = input("Give your file name : ")
    uploadFile(testInput)