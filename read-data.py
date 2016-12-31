import sys
import csv
import facebook
import lxml
import requests

#Facebook token
FB_ACCESS_TOKEN='ADD YOUR ACCESS TOKEN HERE'

#setup facebook graph api
graph = facebook.GraphAPI(access_token=FB_ACCESS_TOKEN)

#constant for the column containting the profile IDs
FB_ID_COLUMN = 2

#open and read the csv fie
with open(sys.argv[1], 'rb') as f:
    #create csv read object
    reader = csv.reader(f)
    i = 0

    #open and write results to new csv
    with open(sys.argv[2], 'w') as output:
        #create csv write object
        ret_val = csv.writer (output)

        #for loop thru the facebook ID and get profile object
        for row in reader:
            try:
                #skips header
                if i != 0:
                    #change this line if you're interested in other data or relations
                    obj = graph.get_object(row[FB_ID_COLUMN])
                    #writes the dict object's items returned from get call
                    ret_val.writerow(obj.items())
            #issues with profile permission caught to check if isolated issue
            except facebook.GraphAPIError:
                #write F to indicate failed access
                ret_val.writerow('F')
            i+=1
