# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:53:33 2021

@author: Marvin
"""
import requests
from bs4 import BeautifulSoup
from os.path  import basename
import re
import time
import pandas as pd
headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    

#Process League Table
#Transfers ohne Leihen und interne Wechsel
# page = "https://www.transfermarkt.de/rasenballsport-leipzig/transfers/verein/23826/saison_id/2021"
# tree = requests.get(page, headers = headers)
# soup = BeautifulSoup(tree.content, 'html.parser')

buli_cl_teams = {
"fcb": ["https://www.transfermarkt.de/fc-bayern-munchen/transfers/verein/27/saison_id/"],
"bvb" : ["https://www.transfermarkt.de/borussia-dortmund/transfers/verein/16/saison_id/"],
"rbl" : ["https://www.transfermarkt.de/rasenballsport-leipzig/transfers/verein/23826/saison_id/"],
"bmg" : ["https://www.transfermarkt.de/borussia-monchengladbach/transfers/verein/18/saison_id/"],
"b04" : ["https://www.transfermarkt.de/bayer-04-leverkusen/transfers/verein/15/saison_id/"],
"hof" : ["https://www.transfermarkt.de/tsg-1899-hoffenheim/transfers/verein/533/saison_id/"],
"wob" : ["https://www.transfermarkt.de/vfl-wolfsburg/transfers/verein/82/saison_id/"],
"s04" : ["https://www.transfermarkt.de/fc-schalke-04/transfers/verein/33/saison_id/"]}

transfers_dict = {"Name": [],
                  "Position": [],
                  "Alter": [],
                  "Marktwert": [],
                  "Abgebender-Verein": [],
                  "Abgebende-Liga": [],
                  "Ablöse": []}

seasons = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

# zugaenge_soup = soup.select("div.box:nth-of-type(3) > div.responsive-table > table > tbody > tr")
# abgaenge_soup = soup.select("div.box:nth-of-type(4) > div.responsive-table > table > tbody > tr")
# print(soup.select("div.box:nth-child(3)"))#" > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr"))
# print(soup)
# s = soup.find("div", {"id": "main"})
# print(s.select("div.box:nth-child(3) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr"))
#main
def createListOfTransfers(transfers_soup, season, team):
    transfers = []
    for transfer_soup in transfers_soup:
        text = transfer_soup.text.strip()
        player = re.split(r'\s{2,}|\n', text)
        player.append(season)
        player.append(team)
        transfers.append(player)
    return transfers

# print(page)
zugaenge = []
for buli_cl_team in [*buli_cl_teams]:
    
    for season in seasons:
        page = buli_cl_teams[buli_cl_team][0]+str(season)
        tree = requests.get(page, headers = headers)
        soup = BeautifulSoup(tree.content, 'html.parser')
        # s = soup.find("div", {"id": "main"})
        zugaenge_soup = soup.select("div.box:nth-child(3) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr")
        # zugaenge_soup = soup.select("div.row > div.large-12 > div.box:nth-of-type(3) > div.responsive-table > table > tbody > tr")
        # print(zugaenge_soup)
        # abgaenge_soup = soup.select("div.box:nth-of-type(4) > div.responsive-table > table > tbody > tr")
        
        zugaenge.extend(createListOfTransfers(zugaenge_soup, season, buli_cl_team))
        # print(zugaenge)
        time.sleep(0.1)
    time.sleep(0.4)
        # abgaenge = createListOfTransfers(abgaenge_soup)
    
# print(zugaenge)   



df = pd.DataFrame.from_records(zugaenge, columns=["Name","Position","Alter","Marktwert","Abgebender-Verein","Abgebende-Liga","Ablöse","Saison","Aufnehmender-Verein"])
print(df)
df.to_csv("C:/Users/Marvin/Desktop/Portfolio/soccer/bayernkaputtkauf/buli-cl-teams-zugaenge.csv", index=False)
