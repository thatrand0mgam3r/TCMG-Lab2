import urllib.request
import os
from collections import Counter

path= './http_access_log.txt'

exists = os.path.exists(path)

#print(exists)
if exists == False:

    print('Seems you are missing some important files...lets get them for you.....')

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url,'./http_access_log.txt')

    file = open("http_access_log.txt")
    data = file.read()

    count1 = data.count(".html")
    count2 = data.count(".gif")
    count3 = data.count(".xbm")
    count4 = data.count(".jpg")
    count5 = data.count(".jpeg")
    count6 = data.count(".ps")

    c = Counter({'html': count1, 'gif': count2, 'xbm': count3, 'jpg': count4, 'jpeg': count5, 'ps': count6})
    d = c.most_common(1)[-1]
    e = c.most_common()[-1]
    print(f'The Least requested file is {e}')
    print(f'The Most common requested file is {d}')
else:
        file= open ("http_access_log.txt")
        data = file.read()

        count1 = data.count(".html")
        count2 = data.count(".gif")
        count3 = data.count(".xbm")
        count4 = data.count(".jpg")
        count5 = data.count(".jpeg")
        count6 = data.count(".ps")

        c = Counter({'html':count1, 'gif':count2, 'xbm':count3, 'jpg':count4 ,'jpeg':count5, 'ps':count6})
        d = c.most_common(1)[-1]
        e = c.most_common()[-1]
        print(f'The Least requested file is { e }')
        print(f'The Most common requested file is { d }' )
