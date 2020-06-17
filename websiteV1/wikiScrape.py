import sys
import requests
import bs4
import datetime
import pymysql
import random

#Information Pipeline:
#parseHTML -> getNewsData() -> newsToSQL() -> genIndex() -> sqlInsert()



#Function that inserts data to sql
def sqlInsert(storyID, indexKey, radii, headline, url, dateAdded):
    db = pymysql.connect("rehodb.cagxsdx2k0ey.us-east-2.rds.amazonaws.com", "admin", "rehoboam")
    cursor = db.cursor()
    sql1 = "INSERT INTO rehoboamSchema.rehoboamReal (storyID, indexKey, source, radii, headline, url, dateAdded, isActive) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    vals = (storyID, indexKey, "real", radii, headline, url, dateAdded, 1)
    cursor.execute(sql1,vals)
    db.commit()
    db.close()
    print("SQL INSERT\n")

#This function generates the index for each story
def genIndex():
    db = pymysql.connect("rehodb.cagxsdx2k0ey.us-east-2.rds.amazonaws.com", "admin", "rehoboam")
    cursor = db.cursor()
    #Change to sort by date added eventually
    sql1 = "SELECT indexKey FROM rehoboamSchema.rehoboamReal ORDER BY indexKey ASC LIMIT 1"
    cursor.execute(sql1)
    result=cursor.fetchone()
    db.close()
    tempIndex = result[0]

    if tempIndex == 6:
        indexKey = 300
    else:
        indexKey = tempIndex - 6

    return indexKey

#This function prepares the inforation for mySQL
def newsToSQL(headline, url, dateAdded):
    
    indexKey = genIndex() #Calls function to generate Index
    storyID = (str(dateAdded) + "." + str(indexKey)) #Creates unique storyID
    radii = random.randint(5000, 20000) #Random height for each story
              #[storyID, indexKey, source, radii, headline, url, dateAdded, isActive]
    sqlArray = [storyID, indexKey, "real", radii, headline, url, dateAdded, "TRUE"] #2D array that will be used to transfer data to mySQL
    print(sqlArray)
    sqlInsert(storyID, indexKey, radii, headline, url, dateAdded)

#This function finds the relevant information
def getNewsData(tempHeadline, dateAdded):

    citeNote = "cite_note-"
    citeNum = tempHeadline.getText()[-4:-1] #Value used to find news source
    citeNote = citeNote + citeNum       

    source = soup.find("li", {"id": citeNote}).find("a", {"class": "external text"})    #Finds source
    headline = source.getText()[1:-1] 
    url = source.get("href")

    newsToSQL(headline, url, dateAdded) #Function that will insert data into database

#Main function that initially parses HTML
def parseHTML(dateAdded, wikiDate, soup):

    monthSpan = soup.find('span', {"id": month})    #Finds span unique to Events sections on page
    spanParent = monthSpan.find_parent("h3")        #Moves up to the parent
    parentSibling = spanParent.find_next_sibling("ul")  #Moves to the next sibling
    todaysNews = parentSibling.find('a', {"title": "June 16"})   #Goes to todays stories

    if str(todaysNews) == "None": #If there is no news for the day
        print("No News")

    else:
        stories = todaysNews.find_next_sibling("ul") #if there is only one story, this will return none
        #If only one story
        if str(stories) == "None":
            tempHeadline = todaysNews.find_parent("li")  #finds headline
            getNewsData(tempHeadline, dateAdded)   #Function returns the headline and URL from today's story

        #If multiple stories
        else:
            tempHeadline = stories.findChildren("li", recursive=False)  #finds all headlines
            for i in range(len(tempHeadline)):      
                getNewsData(tempHeadline[i], dateAdded) #Function returns the headlines and URLs from today's stories


#MAIN/PROGRAM BEGINNING

#gathering date information for wiki scrape
dateAdded = datetime.date.today() 
month = dateAdded.strftime("%B")
day = str(dateAdded.day)

dateAdded = str(dateAdded)  #Cast to string for sql
wikiDate = (month + ' ' + day)  #Current date in wiki friendly format

res = requests.get('https://en.wikipedia.org/wiki/2020')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"lxml")

parseHTML(dateAdded, wikiDate, soup)





