import urllib.request,urllib.parse,urllib.error
fhand = urllib.request.urlopen('https://github.com/VinitChawda06/-Python-Virtual-Assistant-for-Speech-Recognition-and-Task-Automation-')
# count = dict()
for line in fhand:
    print(line.decode().strip().split())
    # words = line.decode().split()
    # for word in words:
        # count[word]=count.get(word,0) + 1
# print(count)