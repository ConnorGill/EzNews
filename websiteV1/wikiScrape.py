import sys
import requests
import bs4
import datetime

#gathering date information for wiki scrape
mydate = datetime.datetime.now() 
year = str(mydate.year)
month = mydate.strftime("%B")
day = str(mydate.day)
wikiDate = (year + '_' + month + '_' + day)
print(wikiDate)

res = requests.get('https://en.wikipedia.org/wiki/Portal:Current_events')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"lxml")

#topics = soup.find('div', {"id": "2020_June_15"}).findAll('div', {"role": "heading"})
links = soup.find('div', {"id": wikiDate}).findAll('a', {"class": "external text"}) #only grabbing links from current day
for i in range(len(links))[3:]: #first three lines are irrelevant
    print(links[i].get('href'))
    #Next steps: pull titles from each link that passes through this
    #Will probably have to create test cases for each major news site due to different markup



