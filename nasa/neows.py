#!/usr/bin/python3
import requests
import pprint
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

#load env vars
load_dotenv()

## Define NEOW UR
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this is our main function
def main():
    #store api key
    nasacreds = "api_key=" + os.getenv("API_KEY")

    ##ask user for date and make request
    startdate = input("please enter a start date (yyyy-mm-dd): ")
    answer= input("would you like to enter a end date? (yes or no): ").lower()
    if answer == 'yes':
        enddate = input("please enter a end date (yyyy-mm-dd): ")
        neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds + "&" + enddate)
    else:
        neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    pprint.pprint(neodata)

if __name__ == "__main__":
    main()

