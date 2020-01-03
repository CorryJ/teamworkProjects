##Teamwork Projects - Getting logged time per project in a set time period##

Programme (python) to get time logs for each project in Teamwork Projects using Teamwork API. 

Specifically this file will:

* Access TeamworkAPI
* Gets all company project id's
* Loops through each id to obtain total time per project in declared fromDate and toDate
* Stores name, id and time totals in a csv
* Uploads CSV to google sheet

**Further info:**
* [Teamwork Projects API v1 documentation](https://developer.teamwork.com/projects/api-v1)
* [Google Sheet / GSpread](https://gspread.readthedocs.io/en/latest/oauth2.html)
