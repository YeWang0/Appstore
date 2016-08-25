from pymongo import MongoClient
import  json

def get_apps_similarity():
    client = MongoClient()
    db = client.appstore

    db_app_info=db.app_info
    db_app_user_similarity=db.app_user_similarity
    db_user_download_history=db.user_download_history

    apps_similarity=dict()

    for x in db_app_info.find():

        app_id=x['app_id']

        for user_similarity in db_app_user_similarity.find({'app_id':app_id}):

            user_id=user_similarity['user_id']
            user_cos_value=user_similarity['cos_similarity']

            for user_download_history in db_user_download_history.find({'user_id':user_id}):

                download_apps=user_download_history['download_history']

                for relat_app_id in download_apps:

                    if relat_app_id!=app_id:
                        if app_id>relat_app_id:
                            #(app_id , relat_app_id)->value+=
                            # (user_id,user_cos_value)
                            two_app_similarity=relat_app_id+'*'+app_id
                            if two_app_similarity in apps_similarity:
                                apps_similarity[two_app_similarity]+=user_cos_value
                            else:
                                apps_similarity.update({two_app_similarity:user_cos_value})

    # file=open('apps_similarity.json','wb')
    # file.write(json.dumps(apps_similarity))

    # Drop the collection if already exist
    if db.apps_similarity.count():
        db.apps_similarity.drop()

    for key,value in apps_similarity.iteritems():
        apps_similarity={'apps_id':key,'apps_cos_similarity':value}
        db.apps_similarity.insert_one(apps_similarity)

get_apps_similarity()
