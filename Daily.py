# Alondra Gonzalez

# Question : How many requests were made on each day? 


import urllib.request
import os

path= './http_access_log.txt'

exists = os.path.exists(path)

def output(filename):
  file = open(filename)
  data = file.read()

  years = ["1994", "1995"]
  months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  # assuming unchanged
  start = 0 # january
  end = 12 # length 

  year = years[0]
  for i in range(9, end):
    if (i == 8 or i == 3 or i == 5 or i == 10): # 30 Sep (8), Apr(3), Jun(5), Nov(10)
      for day in range(1,31):
        printCount(day, months[i], year, data)
    if (i == 0 or i == 2 or i == 6 or i == 4 or i == 9 or i ==7 or i == 11): # 31 Jan(0), Mar(2), Jul(6), May(4), Oct(9), Dec(11), Aug(7)
      startD = 1
      if (i == 9):
        startD = 24
      for day in range(startD,32):
        printCount(day, months[i], year, data)
    if (i == 1): # implying 28 days
      for day in range(1,29):
        printCount(day, months[i], year, data)
  year = years[1]
  for i in range(start, 10):
    if (i == 8 or i == 3 or i == 5 or i == 10): # 30 Sep (8), Apr(3), Jun(5), Nov(10)
      for day in range(1,31):
        printCount(day, months[i], year, data)
    if (i == 0 or i == 2 or i == 6 or i == 4 or i == 9 or i ==7 or i == 11): 
      # 31 Jan(0), Mar(2), Jul(6), May(4), Oct(9), Dec(11), Aug(7)
      for day in range(1,32):
        printCount(day, months[i], year, data)
    if (i == 1): # implying 28 days
      for day in range(1,29):
        printCount(day, months[i], year, data)
  
  
def printCount(day, month, year, data):
  Date = str(day)+"/"+month+"/"+year
  print("The count for", Date, ": ", data.count(Date))


if exists == False:

  print('Seems you are missing some important files...lets get them for you.....')

  url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
  urllib.request.urlretrieve(url,'./http_access_log.txt')
  output("http_access_log.txt")
else:

  output("http_access_log.txt")



