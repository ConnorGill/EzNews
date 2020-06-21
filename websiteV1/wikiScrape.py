import sys
import requests
import bs4
import datetime
import pymysql
import random

#Information Pipeline:
#parseHTML -> getNewsData() -> newsToSQL() -> genIndex() -> sqlInsert()



#Function that inserts data to sql
def sqlInsert(storyID, indexKey, radii, headline, siteurl, dateAdded):
    db = pymysql.connect("rehodb.cagxsdx2k0ey.us-east-2.rds.amazonaws.com", "admin", "rehoboam")
    cursor = db.cursor()
    sql1 = "INSERT INTO rehoboamSchema.rehoboamReal (storyID, indexKey, source, radii, headline, siteurl, dateAdded, isActive, storyAge) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    vals = (storyID, indexKey, "real", radii, headline, siteurl, dateAdded, 1, "newest")
    cursor.execute(sql1,vals)
    db.commit()
    db.close()
    print("SQL INSERT\n")

#This function generates the index for each story
def genIndex():
    db = pymysql.connect("rehodb.cagxsdx2k0ey.us-east-2.rds.amazonaws.com", "admin", "rehoboam")
    cursor = db.cursor()
    #Change to sort by date added eventually
    sql1 = "SELECT storyID, indexKey FROM rehoboamSchema.rehoboamReal WHERE storyAge = 'oldest'"
    cursor.execute(sql1)
    result=cursor.fetchone()
    db.close()
    tempStoryID = result[0]
    tempIndex = result[1]

    print("oldestID = " + str(tempStoryID))
    print("oldestIndex = " + str(tempIndex))
    
    return tempIndex

#This function prepares the inforation for mySQL
def newsToSQL(headline, siteurl, dateAdded):
    
    indexKey = genIndex() #Calls function to generate Index
    storyID = (str(dateAdded) + "." + str(indexKey)) #Creates unique storyID
    radii = random.randint(4500, 10000) #Random height for each story
              #[storyID, indexKey, source, radii, headline, siteurl, dateAdded, isActive]
    sqlArray = [storyID, indexKey, "real", radii, headline, siteurl, dateAdded, "TRUE"] #2D array that will be used to transfer data to mySQL
    print(sqlArray)
    #sqlInsert(storyID, indexKey, radii, headline, siteurl, dateAdded)

#This function finds the relevant information
def getNewsData(tempHeadline, dateAdded):

    citeNote = "cite_note-"
    citeNum = tempHeadline.getText()[-4:-1] #Value used to find news source

    #If no source is given
    if citeNum.isnumeric() == False:
        print("No Source")
    
    else:
        citeNote = citeNote + citeNum       
        source = soup.find("li", {"id": citeNote}).find("a", {"class": "external text"})    #Finds source
        print(source)
        headline = source.getText()[1:-1] 
        headline = headline.upper()
        siteurl = source.get("href")

        newsToSQL(headline, siteurl, dateAdded) #Function that will insert data into database

#Main function that initially parses HTML
def parseHTML(dateAdded, wikiDate, soup):

    monthSpan = soup.find('span', {"id": month})    #Finds span unique to Events sections on page
    spanParent = monthSpan.find_parent("h3")        #Moves up to the parent
    parentSibling = spanParent.find_next_sibling("ul")  #Moves to the next sibling
    todaysNews = parentSibling.find('a', {"title": wikiDate})   #Goes to todays stories

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

#print(wikiDate)
parseHTML(dateAdded, wikiDate, soup)





