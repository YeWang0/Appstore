from pymongo import MongoClient
import json
def get_app_user():
    client = MongoClient()
    db = client.appstore
    app_info=db.app_info
    user_download_history=db.user_download_history
    r1=app_info.find()
    r2=user_download_history.find()
    app_id=[]
    for x in r1:
        app_id.append(x['app_id'])
    # print app_id
    # print len(app_id)
    relat_user=[[]for i in range(len(app_id))]
    app_user=''
    # file=open('app_user.json','wb')
    for i in range(len(app_id)):
        # print i,len(app_id)
        r2=user_download_history.find()
        for x in r2:
            # print(i,x['user_id'])
            if app_id[i] in x['download_history']:
                relat_user[i].append(x['user_id'])
        # print(i,app_id[i],relat_user[i])
        if len(relat_user[i])!=0:
            app_user={'app_id':app_id[i],'relat_user':relat_user[i]}
            db.app_user.insert_one(app_user)