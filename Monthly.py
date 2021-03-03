import urllib.request
import os

path= './http_access_log.txt'

exists = os.path.exists(path)

#print(exists)
if exists == False:

    print('Seems you are missing some important files...lets get them for you.....')

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url,'./http_access_log.txt')


    file = open("http_access_log.txt")
    data = file.read()
    occurrences = data.count("Oct")
    occurrences2 = data.count("Nov")
    occurrences3 = data.count("Dec")
    occurrences4 = data.count("Jan")
    occurrences5 = data.count("Feb")
    occurrences6 = data.count("March")
    occurrences7 = data.count("Apr")
    occurrences8 = data.count("May")
    occurrences9 = data.count("Jun")
    occurrences10 = data.count("Jul")
    occurrences11 = data.count("Aug")
    occurrences12 = data.count("Sep")


    print('Times data was accessed in January:', occurrences5)
    print('Times data was accessed in February:', occurrences6)
    print('Times data was accessed in March:', occurrences7)
    print('Times data was accessed in April:', occurrences8)
    print('Times data was accessed May:', occurrences8)
    print('Times data was accessed in June:', occurrences9)
    print('Times data was accessed in July:', occurrences10)
    print('Times data was accessed in August:', occurrences11)
    print('Times data was accessed in September:', occurrences12)
    print('Times data was accessed October:', occurrences)
    print('Times data was accessed in November:', occurrences3)
    print('Times data was accessed December:', occurrences4)


else:
        file= open ("http_access_log.txt")
        data = file.read()
        occurrences = data.count("Oct")
        occurrences2 = data.count("Nov")
        occurrences3 = data.count("Dec")
        occurrences4 = data.count("Jan")
        occurrences5 = data.count("Feb")
        occurrences6 = data.count("March")
        occurrences7 = data.count("Apr")
        occurrences8 = data.count("May")
        occurrences9 = data.count("Jun")
        occurrences10 = data.count("Jul")
        occurrences11 = data.count("Aug")
        occurrences12 = data.count("Sep")


        print('Times data was accessed in January:', occurrences4)
        print('Times data was accessed in February:', occurrences5)
        print('Times data was accessed in March:', occurrences6)
        print('Times data was accessed in April:', occurrences7)
        print('Times data was accessed May:', occurrences8)
        print('Times data was accessed in June:', occurrences9)
        print('Times data was accessed in July:', occurrences10)
        print('Times data was accessed in August:', occurrences11)
        print('Times data was accessed in September:', occurrences12)
        print('Times data was accessed October:', occurrences)
        print('Times data was accessed in November:', occurrences2)
        print('Times data was accessed December:', occurrences3)
