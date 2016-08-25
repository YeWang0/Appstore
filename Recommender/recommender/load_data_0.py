from pymongo import MongoClient
import json

def load_data(filename):
    client = MongoClient()
    db = client.appstore
    collection=db[filename]
    if collection.count():
        collection.drop()
        collection=db[filename]
    for line_num, line in enumerate(open('../data/'+filename+'.json').readlines()):
        # print line_num
        data = json.loads(line)
        collection.insert_one(data)
load_data('app_info')
load_data('user_download_history')