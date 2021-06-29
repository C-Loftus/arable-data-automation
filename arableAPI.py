import dotenv
from dotenv.main import load_dotenv
import os, requests
import arablepy
from requests.sessions import session
import serialNums
import sys
import json
from base64 import b64encode

# def main():
    # client = arablepy.ArableClient()

    # dotenv.load_dotenv()
    # username = os.environ.get("USERN")
    # password = os.environ.get("PASSW")
    # if username == None or password == None:
    #     sys.exit("No password / username")

    # client.connect(email=username, password=password)
    # client.schema('daily', df=True)

    # # tomato = serialNums.private.data()["AA ChTom"] 
    # # same as above, just hardcoded to show example
    # tomato = "C003649"

    # values = client.data(
    #                 'daily',
    #                 devices= [tomato],
    #                 # order='time',
    #                 start_time="2021-06-03T00:00:00Z",
    #                 end_time="2021-06-17",
    #                 df = True)


    # print(values)
    # return values
    # ^^ always returns/prints an empty dataframe for some reason

def callAPI():
    dotenv.load_dotenv()
    username = os.environ.get("USERN")
    password = os.environ.get("PASSW")

    token = b64encode("{0}:{1}".format(username, password).encode('utf-8')).decode('utf-8')

    r = requests.get("https://api.arable.cloud/api/v2/devices", headers={"Authorization": "Basic " + token})


    # alternative way to get the token
        # curl -X POST \
        #  https://api.arable.cloud/api/v2/auth/token \
        #  -H 'Content-Type: application/json' \
        #  -d '{"email": "<email address>", "password": "<plaintext password>"}'
        # 
    # r = requests.post("https://api.arable.cloud/api/v2/auth/token", headers={"Content-Type" : "application/json"},
    #  data={"email": username, "password": password})


  
    # Initialize JSON data

    
    # Create Python object from JSON string data
    obj = r.json()
    
    # Pretty Print JSON
    json_formatted_str = json.dumps(obj, indent=4)
    print(json_formatted_str)

    print(r.encoding)

if __name__ == "__main__":
    callAPI()










# d = date.today()

# devices = list(serialNums.private.data())

# dataFrame = client.data('daily', devices=devices, start_time='2021-06-05', end_time=d, df=True)
# dataFrame.to_csv("output.csv")







# token = bs.b64encode("{0}:{1}".format(username, password).encode('utf-8')).decode('utf-8')

# i = requests.get("https://api.arable.cloud/api/v2/auth/token")
# x = requests.get("https://api.arable.cloud/api/v2/devices")
# print(x)