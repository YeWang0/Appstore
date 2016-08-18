from pymongo import MongoClient
client = MongoClient()
db = client.appstore

db_app_info=db.app_info
db_app_user_similarity=db.app_user_similarity
db_user_download_history=db.user_download_history

db_top5=db.top5_recommend
db_app_user=db.app_user
s=set()
for x in db_app_user.find():
    if  x['app_id'] in s:
        print x["app_id"],"duplicate"
    else:
        s.add(x['app_id'])

print len(s)
for x in db_top5.find():
    if x['app_id'] not in s:
        print x['app_id']


