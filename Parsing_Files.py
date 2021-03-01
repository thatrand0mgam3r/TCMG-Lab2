#Please enter code here for the parsing log assignment

#When you submit your part please comment your name and what section you had for accountability.

#This next section is done by Nhat-Tien Nguyen
#This section answers, "What percentage of the requests were redirected elsewhere (any 3xx codes)?"
import urllib.request
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
pastyear = data.count('1994')
all = data.count("1995")
total = pastyear + all
total1 = redirect + redirect1 + redirect2 + redirect3 + redirect4 + redirect5 + redirect6
percentage = total1/total

answer = input ("Would you like to see the percentage of requests that were redirected? ")
if answer == "yes":
    print("{:.2%}".format(percentage))
elif answer == "no":
    print ("Thank you for your time.")


