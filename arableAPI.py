from typing import List
import dotenv
from dotenv.main import load_dotenv
import os, requests
from requests.api import request
from requests.sessions import session
import serialNums
from base64 import b64encode

# simple comma sep. concatenation 
def generateSelectParam(input: List):
    output = ""
    for i in range(len(input)):
        output += input[i]

        # i don't want a comma at the end. Python length isn't 0 
        # indexed so we need to take minus 1
        if i != len(input) - 1:
            output += ","
    return output
        

def callAPI():
    dotenv.load_dotenv()
    username = os.environ.get("USERN")
    password = os.environ.get("PASSW")

    token = b64encode("{0}:{1}".format(username, password).encode('utf-8')).decode('utf-8')

    for sensor in serialNums.private.data():
        # temp = generateSelectParam(serialNums.private.arableDefaultOutput)
        params = {
            'ratio': 'dec',
            'temp': 'F',
            'pres': 'mb',
            'size': 'in',
            'local_time': 'America/New_York',
            'ratio': 'dec',
            'device': serialNums.private.data()[sensor],
            # all of the column names we want
            'select': 'device,cl,etc,ndvi,swdw,maxt,meant,mint,precip,crop_water_demand,lfw'
        }

        headers = {"Authorization": "Basic " + token,
                    "Accept": "text/csv"
                    }

        r = requests.get("https://api.arable.cloud/api/v2/data/daily", 
            params=params, headers=headers)

        print("Getting data from", sensor)
        with open('filesToReadThenDelete/' + str(sensor), 'wb') as f:
            f.write(r.content)



  


if __name__ == "__main__":
    # test = ["1", "2", "3"]
    # print(generateSelectParam(test))
    # print(generateSelectParam(serialNums.private.arableDefaultOutput))
    callAPI()
