import urllib.request
import os

path= './http_access_log.txt'

exists = os.path.exists(path)

#print(exists)
if exists == False:

    print('Grabbing missing files...')

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url,'./http_access_log.txt')

file = open("http_access_log.txt")
data = file.read()
redirect = data.count('" 300 ')
redirect1 = data.count('" 301 ')
redirect2 = data.count('" 302 ')
redirect3 = data.count('" 303 ')
redirect4 = data.count('" 304 ')
redirect5 = data.count('" 305 ')
redirect6 = data.count('" 306 ')
redirect7 = data.count('" 307 ')
redirect8 = data.count('" 308 ')
total1 = redirect + redirect1 + redirect2 + redirect3 + redirect4 + redirect5 + redirect6 + redirect7 + redirect8

file = open("http_access_log.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1

percentage = total1/line_count
file.close()

print("{:.2%}".format(percentage) + " of requests were redirected.")
