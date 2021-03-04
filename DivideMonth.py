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
input = open("http_access_log.txt","r")
outputJan = open("JanuaryLog.txt", "w")
outputFeb = open("February.txt", "w")
outputMar=open("March.txt","w")
outputApr=open("April.txt","w")
outputMay=open("May.txt","w")
outputJun=open("June.txt","w")
outputJul=open("July.txt","w")
outputAug=open("August.txt","w")
outputSep=open("September.txt","w")
outputOct=open("October.txt","w")
outputNov=open("November.txt","w")
outputDec=open("December.txt","w")



for line in input:
    if "/Jan/" in line:
        outputJan.write(line)
    elif"/Feb/" in line:
        outputFeb.write(line)
    elif"/Mar/" in line:
        outputMar.write(line)
    elif "/Apr/" in line:
        outputApr.write(line)
    elif "/Jun/" in line:
        outputJun.write(line)
    elif "/Jul/" in line:
        outputJul.write(line)
    elif "/Aug/" in line:
        outputAug.write(line)
    elif "/Sept/" in line:
        outputSep.write(line)
    elif "/Oct/" in line:
        outputOct.write(line)
    elif "/Nov/" in line:
        outputNov.write(line)
    elif "/Dec/" in line:
        outputDec.write(line)


else:
        file= open ("http_access_log.txt")
        data = file.read()

        print("We will now seperate the file into months. Each Month will be put in a file with it's name.")
        input = open("http_access_log.txt", "r")
        outputJan = open("JanuaryLog.txt", "w")
        outputFeb = open("February.txt", "w")
        outputMar = open("March.txt", "w")
        outputApr = open("April.txt", "w")
        outputMay = open("May.txt", "w")
        outputJun = open("June.txt", "w")
        outputJul = open("July.txt", "w")
        outputAug = open("August.txt", "w")
        outputSep = open("September.txt", "w")
        outputOct = open("October.txt", "w")
        outputNov = open("November.txt", "w")
        outputDec = open("December.txt", "w")

        for line in input:
            if "/Jan/" in line:
                outputJan.write(line)
            elif "/Feb/" in line:
                outputFeb.write(line)
            elif "/Mar/" in line:
                outputMar.write(line)
            elif "/Apr/" in line:
                outputApr.write(line)
            elif "/Jun/" in line:
                outputJun.write(line)
            elif "/Jul/" in line:
                outputJul.write(line)
            elif "/Aug/" in line:
                outputAug.write(line)
            elif "/Sept/" in line:
                outputSep.write(line)
            elif "/Oct/" in line:
                outputOct.write(line)
            elif "/Nov/" in line:
                outputNov.write(line)
            elif "/Dec/" in line:
                outputDec.write(line)

        print("Done....Now please check your folder/directory for the new files.")