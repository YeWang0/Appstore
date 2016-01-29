from pymongo import MongoClient
from math import sqrt
import json
def cos_app_user(app_id,user_id):
    # print app_id,user_id
    d=user_download_histroy.find({'user_id':user_id})
    for t in d:
        cos_similarity=sqrt(len(t.get('download_history')))
    app_user_similarity={'app_id':app_id,'user_id':user_id,'cos_similarity':cos_similarity}
    file.write(json.dumps(app_user_similarity))

app_user=''
file=open('app_user_similarity.json','wb')
client = MongoClient()
db = client.appstore
app_info=db.app_info
user_download_histroy=db.user_download_histroy
app_user=db.app_user
r1=app_info.find()
r2=user_download_histroy.find()
r3=app_user.find()
for x in r3:
    # print(x['relat_user'])
    for user_id in x['relat_user']:
        cos_app_user(x['app_id'],user_id)


