import json
import os
import glob
import pprint
keywordList = []
filename = 'message_1(13).json'
##for filename in glob.glob(os.path.join(path, '*.json')): only process .JSON files in folder.      
f = open("backend\message_1 (13).json", "r")
data=f.read().replace('\n', '')
keyword = json.loads(data)
keyword=keyword["messages"]
for x in keyword:
        print(x.get("content"))
