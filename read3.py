import urllib2,json,base64
accesstoken ="2PMBD1Z8JHF7H91051D3"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTIme/Statistics.json".format(institution,course)
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response = urllib2.urlopen(request)
data = json.load(response)
print json.dumps(data,indent=2)
