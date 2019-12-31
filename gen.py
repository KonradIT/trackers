import os, json
for tracker in os.listdir("trackers"):
	content = json.loads(open("trackers/%s" % tracker).read())
	if content.get("enabled"):
		for url in content.get("url"):
			print("%s %s" % ("0.0.0.0", url))