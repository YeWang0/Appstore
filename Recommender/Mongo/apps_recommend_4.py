from pymongo import MongoClient
import  json

def get_apps_recommend():
    client = MongoClient()
    db = client.appstore

    db_app_info=db.app_info
    db_app_user_similarity=db.app_user_similarity
    db_user_download_history=db.user_download_history
    db_apps_similarity=db.apps_similarity

    def get_relate_app(app_id,s,index):
        if index==0:
            return s[s.find('*')+1:]
        else:
            return s[:s.find('*')]

    recommend=[[]for i in range(db_app_info.find().count())]

    def get_top5(app_dict,values):
        r=[]
        if len(values)<5:
            for v in set(values):
                for id,value in app_dict.iteritems():
                    if value==v:
                        r.append(id)
        else:
            for v in set(values[:5]):
                for id,value in app_dict.iteritems():
                    if value==v:
                        r.append(id)
        return r



    i=0
    apps_dict=[]
    for app_info in db_app_info.find():
        app_id=app_info['app_id']
        # print(app_id)
        app_dict=dict()
        values=[]
        for x in db_apps_similarity.find():
            index=x['apps_id'].find(app_id)
            if index!=-1:
                app_dict.update({get_relate_app(app_id,x['apps_id'],index):x['apps_cos_similarity']})
                values.append(x['apps_cos_similarity'])
        #save all related apps to db->related_apps
        if app_dict:
            s=''
            for key,result in app_dict.iteritems():
                s+=json.dumps({'app_id':key,'value':result})
            db.related_apps.insert_one({'app_id':app_id,'related_apps':s})
        #
            values=sorted(values,reverse=True)
            recommend[i]=get_top5(app_dict,values)
            db.top5_recommend.insert_one({'app_id':app_id,'top5':recommend[i][:5]})
        i+=1

