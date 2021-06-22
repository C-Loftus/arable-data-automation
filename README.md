# Arable-Data-Automation
### About
This summer I worked with Princeton's High Meadow's Environmental Institute to gather and process data about different agricultural practices around the state of New Jersey.

This repository holds the code that was used for automating the data processing. It gathers data from remote field sensors made by Arable, exports it using the Arable API, processes it into a new CSV format, and uploads it to Google Drive with the Drive API so our team can all view it.  

### How to use
* Download arable daily .csv files in Fahrenheit with normal export settings. Download only the dates you want to append
* Install dependencies
```
pip install -r requirements.txt 
```
* Create a conf folder and put your client_secrets.json inside of it.
* Change .sampleDotEnv to .env and put your username and password inside of it.
* Run the program with the first argument as the file you want to append to and the first file as the one you will draw data from.
* Change the serialNums.py file (private, not uploaded to github since it contains secrets) to the folder path on Google Drive you want.

### Status
My internship will continue until the end of the summer, so this project is still a work in progress and will be adapted depending on what the team needs.

