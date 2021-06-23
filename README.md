# Arable-Data-Automation
### About
This summer I worked with Princeton's High Meadow's Environmental Institute to gather and process data about different agricultural practices around the state of New Jersey.

This repository holds the code that was used for automating the data processing. It gathers data from remote field sensors made by Arable, exports it using the Arable API, processes it into a new CSV format, and uploads it to Google Drive with the Drive API so our team can all view it.  

### How to setup
* Requirements: Python3, pip3, bash (for optional setupWizard.sh), requests==2.22.0, PyDrive==1.3.1, arablepy==0.1, python-dotenv==0.18.0
* Download arable daily .csv files in Fahrenheit with normal export settings. Download only the dates you want to append
* Run the setup script or manually install dependencies and setup credentials.

#### Automatic Setup
```
chmod +x setupWizard.sh
./setupWizard.sh
```
#### Manual Setup
where $name and $pass are your arable username and password
```
mkdir conf/
cp pathToClientSecrets/client_secrets.json conf/.
echo "USERN=$name" >> .env
echo "PASSW=$pass" >> .env
pip install -r requirements.txt 
```
### How to run.
* Run the program with the first argument as the file you want to append to and the first file as the one you will draw data from.
```
# where foo.csv is the csv file you are adding data to and where bar.csv is the csv file you are drawing data from
python3 main.py foo.csv bar.csv 
```
* Change the serialNums.py file (private, not uploaded to github since it contains secrets) to include the folder path on Google Drive you want or any extra sensors

### Status
My internship will continue until the end of the summer, so this project is still a work in progress and will be adapted depending on what the team needs.

