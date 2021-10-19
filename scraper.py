from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd

headerAdded = False

for yr in range(1970,2021):
    myurl = f'https://www.pro-football-reference.com/years/{yr}/games.htm'
    # grab website 
    uClient = uReq(myurl)
    

    # read / close HTML
    page_html = uClient.read()
    uClient.close()
     
    # getting BeautifulSoup 
    soup= bs(page_html, "html.parser")
    #print(page_soup.prettify())
    
    #Week column
    weeksList=[]

    weeks = soup.findAll(
       "th", {"data-stat": "week_num"})
    for tag in weeks:
        txt= tag.text;
        weeksList.append(txt) 
    weeksList= [val for val in weeksList if val != 'Week' ]    
#    weeksist = datesList[1:]#dropping the first index because it's accidently pulling in the header

#   Day Column 
    dayList=[]
    day = soup.findAll(
       "td", {"data-stat": "game_day_of_week"})
    for tag in day:
        txt= tag.text;
        dayList.append(txt) 
    
    #Getting "Date" column
    datesList=[]
    dates = soup.findAll(
       "td", {"data-stat": "game_date"})
    for tag in dates:
        txt= tag.text;
        datesList.append(txt) 
 #   datesList = datesList[1:]#dropping the first index because it's accidently pulling in the header
        
    #Getting Time column
    startList=[]
    startTimes= soup.findAll(
       "td", {"data-stat": "gametime"})
    for tag in startTimes:
        txt= tag.text;
        startList.append(txt)      
       
    #Getting "winner/tie"" column
    winningTeamsList =[]
    winningNames = soup.findAll(
       "td", {"data-stat": "winner"})
    for tag in winningNames:
        txt= tag.text;
        winningTeamsList.append(txt)  
        
    #Getting "@" column
    locationList =[] 
    locations= soup.findAll(
       "td", {"data-stat": "game_location"})
    for tag in locations:
        txt= tag.text;
        locationList.append(txt)   
        
    #Getting "loser/tie"" column
    losingTeamsList =[]
    losingNames = soup.findAll(
       "td", {"data-stat": "loser"})
    for tag in losingNames:
        txt= tag.text;
        losingTeamsList.append(txt)  

        
    #Getting "pts/w" column
    ptsWinnerList =[] 
    pts= soup.findAll(
       "td", {"data-stat": "pts_win"})
    for tag in pts:
        txt= tag.text;
        ptsWinnerList.append(txt)      

    #Getting "pts/l" column
    ptsLoserList =[] 
    pts= soup.findAll(
       "td", {"data-stat": "pts_lose"})
    for tag in pts:
        txt= tag.text;
        ptsLoserList.append(txt)     

    #Getting "yards_win" column
    yardsWinList =[] 
    yardsWin= soup.findAll(
       "td", {"data-stat": "yards_win"})
    for tag in yardsWin:
        txt= tag.text;
        yardsWinList.append(txt)   
        
     #Getting "TOW" column
    homeTurnoverList =[] 
    homeTO= soup.findAll(
       "td", {"data-stat": "to_win"})
    for tag in homeTO:
        txt= tag.text;
        homeTurnoverList.append(txt) 
        
    #Getting "yards_lose" column
    yardsLoseList =[] 
    yardsLose= soup.findAll(
       "td", {"data-stat": "yards_lose"})
    for tag in yardsLose:
        txt= tag.text;
        yardsLoseList.append(txt)   
        
  #Getting "TOL" column
    awayTurnoverList =[] 
    awayTO= soup.findAll(
       "td", {"data-stat": "to_win"})
    for tag in awayTO:
        txt= tag.text;
        awayTurnoverList.append(txt)  

    header= ['Season', 'Week', 'Day', 'Date', 'Time','Winner/Tie', 'Location', 'Loser/Tie', 'Points_Winner','Points_Loser', 'Yards_Winner', 'Turnover_Winner', 'Yards_Loser','Turnover_Loser' ]
    with open('nflFullGameLog.csv','a') as file:
            #writing to csv file
            writer=csv.writer(file)
            if not headerAdded:
                writer.writerow(header)
                headerAdded= True
            for i in range(len(datesList)):    
                myRow= [ yr, weeksList[i], dayList[i], datesList[i],startList[i],winningTeamsList[i],locationList[i],losingTeamsList[i],ptsWinnerList[i],ptsLoserList[i],yardsWinList[i], homeTurnoverList[i],yardsLoseList[i], awayTurnoverList[i] ]
                writer.writerow(myRow)

#df= pd.read_csv('nflGameLog2010.csv') #reading in csv