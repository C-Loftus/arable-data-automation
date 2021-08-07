# Arable-Data-Automation
### About
During the summer of 2021 I worked with Princeton University's High Meadow Environmental Institute to gather and process data about different agricultural practices around the state of New Jersey.

This repository holds the code that was used for automating the data processing. It gathers data from remote field sensors made by Arable, exports it using the Arable API, processes it into a new CSV format, and uploads it to Google Drive with the Drive API so our team can all view it.  

### How to setup
* Requirements: Python3, pip3, bash (for optional setupWizard.sh), requests==2.22.0, PyDrive==1.3.1, arablepy==0.1, python-dotenv==0.18.0 (though Python dependencies are of course automatically handleded by requirements.txt and pip3)
* serialNums.py : This is a file not in this repo for security purposes. It is located in the shared Google Drive since it has private info like farm names and Arable sensor serial numbers. Contact me if  you for some reason don't have access to this. 
* Download arable daily .csv files in Fahrenheit with normal export settings. Download only the dates you want to append
* Run the setup script or manually install dependencies and setup credentials.

#### Automatic Setup
```
chmod +x setupWizard.sh
./setupWizard.sh
```
#### Manual Setup
where $name and $pass are your arable username and password and where pathToClientSecrets is the path to the client_secrets.json file
```
mkdir conf/
cp pathToClientSecrets/client_secrets.json conf/.
echo "USERN=$name" >> .env
echo "PASSW=$pass" >> .env
pip install -r requirements.txt 
```
### How to run.
* The program can be ran either manually or with two argument inputs or automatically by downloading the files to use from the team drive.
* To use it manually, run the program with the first argument as the file you want to append to and the second file as the one you will draw data from.
```
# where foo.csv is the csv file you are adding data to and where bar.csv is the csv file you are drawing data from
python3 main.py foo.csv bar.csv 
```
* To run with automatic downloads, just run the main.py file
```
python3 main.py
```
* For correct behavior, change the serialNums.py file (private, not uploaded to github since it contains secrets) to include the folder path on Google Drive you want or any extra sensors. Make sure you have the correct directory structure, as shown in the setup wizard and README. 

If you are a future year's team and need access to serialNums.py, please email me. 

### Status
This program is stable and essentially finished to coincide with the completion of my internship. 
