import urllib.request
import os
#creates path
path= './http_access_log.txt'
# checks to see if path exists
exists = os.path.exists(path)

#if path does not exist
if exists == False:

    print('Grabbing missing files...')

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url,'./http_access_log.txt')
#opens the file
file = open("http_access_log.txt")
#reads the file
data = file.read()
# counts the number of times a 404 status code happened (unsuccessful requests)

unsuccessful = data.count('" 404 ')

#counts the number of requests in the log
file = open("http_access_log.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
# calculates the percentage of unsuccessful requests
percent = unsuccessful/line_count
file.close()

print("{:.2%}".format(percent) + " of requests were not successful.")
