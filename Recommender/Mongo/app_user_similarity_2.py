from pymongo import MongoClient
from math import sqrt
import json
def get_app_user_similarity():
    def cos_app_user(app_id,user_id):
        # print app_id,user_id
        d=user_download_history.find({'user_id':user_id})
        for t in d:
            cos_similarity=sqrt(len(t.get('download_history')))
        app_user_similarity={'app_id':app_id,'user_id':user_id,'cos_similarity':cos_similarity}
        # file.write(json.dumps(app_user_similarity))
        db.app_user_similarity.insert_one(app_user_similarity)

    # file=open('app_user_similarity.json','wb')
    client = MongoClient()
    db = client.appstore

    app_user=db.app_user
    user_download_history=db.user_download_history
    result=app_user.find()
    for x in result:
        # print(x['relat_user'])
        for user_id in x['relat_user']:
            cos_app_user(x['app_id'],user_id)


