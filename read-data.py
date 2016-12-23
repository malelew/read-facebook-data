import sys
import csv
import facebook
import lxml
import requests

#Facebook token
FB_ACCESS_TOKEN=''

#setup facebook graph api
graph = facebook.GraphAPI(access_token=FB_ACCESS_TOKEN)

#open and read the csv fie
with open(sys.argv[1], 'rb') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i != 0:
            obj = graph.get_object(row[0])
            print obj
        i+=1

