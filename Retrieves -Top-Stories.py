#------------------------------------------------------------------------------------------------------
# 1) Retrieves "Top Stories" from this parliament data RSS feed endpoint: 
# 2) Outputs a CSV file of the data.
#-------------------------------------------------------------------------------------------------------

import csv
import requests
import xml.etree.ElementTree as ET
  
def loadurl():
  
    top_stories_url = 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml'
    
    respose = requests.get(top_stories_url)
    
    with open('topstories.xml', 'wb') as f:
        f.write(respose.content)
          
  
def parseXML(datafile):
  
    tree = ET.parse(datafile)
    root = tree.getroot()
    newsitems = []
  
    # iterate news items
    for item in root.findall('./item/title/'):
  
        news = {}
  
        # iterate child elements of item
        for child in item:
  
            # checking for object content:media
            title =x.find('title').text
  
        # append news dictionary to news items list
        newsitems.append(news)
      
    # return news items list
    return newsitems
  
  
def save_csv(newsitems, filename):
  
    # specifying the fields for csv file
    fields = ['title']
  
    with open(filename, 'w') as csvfile:
  
        writer = csv.DictWriter(csvfile, fieldnames = fields)
  
        writer.writeheader()
  
        # writing data 
        writer.writerows(newsitems)
  
      
def main():
    # load rss from web to update existing xml file
    loadurl()
  
    # parse xml file
    newsitems = parseXML('topstories.xml')
  
    # store news items in a csv file
    save_csv(newsitems, 'topstories.csv')
      
      
if __name__ == "__main__":
    main()
    
 #-------------------------------------------------------------------------------------------------------
 # Reference : Stack OverFlow , Geeksforgeeks
 #-------------------------------------------------------------------------------------------------------
