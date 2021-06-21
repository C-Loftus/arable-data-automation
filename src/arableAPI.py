import dotenv
import base64 as bs
from datetime import date
from dotenv.main import load_dotenv
import os, requests
import arablepy
import pandas as pd
from requests.sessions import session
import serialNums
import sys


client = arablepy.ArableClient()

dotenv.load_dotenv()
username = os.environ.get("USERN")
password = os.environ.get("PASSW")
if username == None or password == None:
    sys.exit("No password / username")

client.connect(email=username, password=password)
client.schema('daily', df=True)

tomato = serialNums.private.data()["AA ChTom"]
# print(tomato)
tomato = "C003649"

values = client.data(
                'daily',
                devices= [tomato],
                # order='time',
                start_time="2021-06-03T00:00:00Z",
                end_time="2021-06-17",
                df = True)


print(values)
# ^^ always returns an empty dataframe for some reason















# d = date.today()

# devices = list(serialNums.private.data())

# dataFrame = client.data('daily', devices=devices, start_time='2021-06-05', end_time=d, df=True)
# dataFrame.to_csv("output.csv")







# token = bs.b64encode("{0}:{1}".format(username, password).encode('utf-8')).decode('utf-8')

# i = requests.get("https://api.arable.cloud/api/v2/auth/token")
# x = requests.get("https://api.arable.cloud/api/v2/devices")
# print(x)