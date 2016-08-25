from app_user_1 import get_app_user
from app_user_similarity_2 import get_app_user_similarity
from apps_similarity_3 import get_apps_similarity
from apps_recommend_4 import get_apps_recommend
from load_data_0 import load_data
if __name__ == "__main__":
    print "Recommend top 5 apps for apps huawei app store!"
    print "-----------------------------------------------"
print " **Load data **"
load_data('app_info')
load_data('user_download_history')
print " **Get app_user **"
get_app_user()
print " **Get app_user_similarity **"
get_app_user_similarity()
print " **Get apps_similarity **"
get_apps_similarity()
print " **Get related_apps and top5_recommend **"
get_apps_recommend()

print "Done!Data has been written into Mongodb.appstore"
print "-----------------------------------------------"
print "Related Tables:"
print " ** app_info"
print " ** user_download_history"
print " ** app_user_similarity"
print " ** apps_similarity"
print " ** related_apps"
print " ** top5_recommend"

