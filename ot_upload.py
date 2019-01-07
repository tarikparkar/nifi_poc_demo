import requests
from requests.auth import HTTPDigestAuth,HTTPBasicAuth
url = 'http://otxecmdemo.opentext.net/otcs/cs.exe/api/v1/nodes'
file = {'type':'144','parent_id':'59597','name':'Migratefile', 'file':'c:\tparkarfiles\nifi\d.txt'}
auth=HTTPBasicAuth('admin','livelink')
r = requests.post(url,files=file,auth=auth)
print(r)
#system url which does not work- not to add this code to the nifi framework
#sys.path.insert(0,"C:\\Users\\tparkar\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages\\requests")
