#import modules
import urllib3
import json
from pandas.io.json import json_normalize
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import datetime
import certifi
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

#authentication details
company = "xxxxxxxx" #add your teamwork projects api credentials
key = "xxxxxxxx"

f = open("xxxxxxxx.csv", "w")
f.truncate()
f.close()

#GETS ALL PROJECT IDS AND STORES AS VARIABLE TO USE IN
actionProjId = "projects.json?pageSize=500" #the api url
urlProjNo = "https://{0}.teamwork.com/{1}".format(company, actionProjId)
headers = urllib3.util.make_headers(basic_auth=key + ":xxx")
request = http.request('GET', urlProjNo, headers=headers)
dataProj = json.loads(request.data)
data_out_Proj = json_normalize(dataProj, ['projects'])

#print(data_out_Proj['id'])
#FINAL STORED VARIABLE
ProjID = (data_out_Proj['id']) #only use to get all projectID's

#for i in ProjID:
    #print(i)

#ProjID = [xxxxxx,xxxxxx,xxxxxx] # individual Teamwork projectID's

#dates query parameters in yyyymmdd format
fromDate = 20200101
toDate = 20200131

for client_id in ProjID:
    action = "/projects/{0}/time/total.json?fromDate={1}&toDate={2}".format(client_id, fromDate, toDate)
    headers = urllib3.util.make_headers(basic_auth=key + ":xxx")
    url = "https://{0}.teamwork.com/{1}".format(company, action)
    request = http.request('GET', url, headers=headers)
    data = json.loads(request.data)
    keytest = 'projects'
    try:
        data_out = json_normalize(data[keytest], errors='ignore') #flattens nested json type structure
        print(data_out)
    except KeyError:
        print(client_id+" error")
    data_out.to_csv("xxxxxxxx.csv", columns=('name','id','time-totals.billable-hours-sum'), mode='a', encoding='utf-8', index=False, header=False)

#google api csv import of outputed data to google sheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/xxxxxxxx/xxxxxxxx/creds.json", scope) #location of credentials file
client = gspread.authorize(creds)

content = open('xxxxxxxx.csv', 'r').read()
client.import_csv('YOURGOOGLESHEETKEY', content) #id of google sheet

sheet = client.open('Projects_Time').sheet1
time = str(datetime.datetime.now())

sheet.update_acell('J1', "Last updated: " +time)
print(time)






