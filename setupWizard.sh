#!/usr/bin/env bash
echo -e "\n*********************************
Welcome to the Arable Automator Setup Wizard
This will make sure you have the correct credentials set up to run the program.
Go slow through this process, as mistyping credentials will prevent you from eventually being able to query the Google/Arable APIs.\n"

read -n 1 -s -r -p "Press any key to continue"

echo -e "\n*********************************
Installing Python Dependencies."

which Python3 
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error you don't have Python3 installed. Please install it then rererun the script"
    exit 1
fi

which pip3
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error you don't have the Python3 package mangager, pip3, installed. 
    Please install pip3 then rererun the script"
    exit 1
fi

pip3 install -r requirements.txt
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error installing packages. Check that requirements.txt is in this directory."
    exit 1
fi

echo -e "\n*********************************
Now, you must create an OAuth client for this application
Then, enable the Drive API on your Google account.
This is to upload files automatically with PyDrive.\n
Watch this video for instructions:\n
https://youtu.be/skxmmMWJ0O8"

read  -p "Press Space when finished or press Ctrl-C to quit the setup for the time being."

echo -e "\n*********************************
Checking directory structure. Looking for a conf/ folder and .dotenv file ...\n"

if [ -d "/conf" ]; then
    echo "/conf folder found."
else
    "conf folder not found, creating it now."
    mkdir conf
fi

read  -p "If it is not there already, move the client_secrets.json from the Google OAuth dashboard
into the conf/ file in this directory. Press space when you are finished"

if [ -f "conf/client_secrets.json" ]; then
    echo "client_secrets.json file was found successfully. "
else
    "client_secrets.json not found in conf/
Please rerun the script after placing it there"
    exit 1
fi

echo "The script will now setup your Arable credentials to enable API queries"
echo "These will be stored in your .env file. Do not upload this to a github repo."
echo "Enter your username:"
read name
echo "Enter your password:"
read pass
if [ -f ".env" ]; then
    echo ".env file found, passing in credentials"
    echo "USERN=$name" >> .env
    echo "PASSW=$pass" >> .env
else
    ".env file not found, creating it now and then passing in credentials"
    touch .env
    echo "USERN=$name" >> .env
    echo "PASSW=$pass" >> .env
fi

echo "Setup finished successfully."
echo "Consult the README.md file on instructions for running the program."

