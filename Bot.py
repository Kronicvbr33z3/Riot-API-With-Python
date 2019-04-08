import requests
import json
from decimal import Decimal
"""
Tool that will provide information about a summoner in python
"""
RIOT_API_KEY = 'RGAPI-13f58c4b-2b86-455b-bd31-c49c62866531'
status = "OK"
print("League of Legends Tool!")
print("Made by Kronic, Version: 0.3")
print("----------------------------------")

def analyzeMatch(matchId):
    print("Match ID: " + str(matchId))
    print()
    MatchURL = 'https://na1.api.riotgames.com/lol/match/v4/matches/' + str(matchId) + '?api_key=' + RIOT_API_KEY
    match_json = requests.get(MatchURL).json()
    
    print("~Match Overview~")
    
    i = 0
    userId = 0
    start = False
    check = True

    while i <= 9:
        tempId = match_json['participantIdentities'][i]['participantId']
        tempPlayer = match_json['participantIdentities'][i]['player']['summonerName']
        tempKills = match_json['participants'][i]['stats']['kills']
        tempDeaths = match_json['participants'][i]['stats']['deaths']
        tempAssists = match_json['participants'][i]['stats']['assists']
        
        tempCS010 = match_json['participants'][i]['timeline']['creepsPerMinDeltas']['0-10']
        tempCS1020 = match_json['participants'][i]['timeline']['creepsPerMinDeltas']['10-20']
        TempCS = (tempCS010 + tempCS1020) / 2
        TempCSRounded = round(TempCS, 2)
        
        if tempPlayer == Summoner_Raw:
          userId = tempId
        
        if i > 4:
            team = 2
            if check:
                start = False
                check = False
            
        else:
            team = 1

        if start == False:
            print()
            print("~TEAM  " + str(team) + "~")
    
            start = True
        
        print(tempPlayer + " " + str(tempKills) + "/" + str(tempDeaths) + "/" + str(tempAssists) + " (" + str(TempCSRounded) + ")")
        
        i += 1
        #print(tempData)
    print("----------------------")
    print()
    
def matchHistory(id):
    print("Showing Match History for " + Summoner_Raw)
    MatchHistory = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + str(id) + "?endIndex=20&beginIndex=0&" +'api_key=' + RIOT_API_KEY 
    match_history_json = requests.get(MatchHistory).json()
    cMatches = 0
    while cMatches <= 20:
        tempChampId = match_history_json['matches'][cMatches]['champion']
        
        tempChampionURL = 'https://na1.api.riotgames.com/lol/static-data/v4/champions/' + str(tempChampId) + '?locale=en_US&api_key=' + RIOT_API_KEY
        tempChamp_json = requests.get(tempChampionURL).json()
        try:
            champ = tempChamp_json['name']
        except:
            print("Riot API Error")
            break
        print("(" + str(cMatches) + ") Champion: " + champ)
        cMatches += 1
    matchChoice = int(input("Choose which match you want to analyze: "))
    matchId = match_history_json['matches'][matchChoice]['gameId']



    analyzeMatch(matchId)
        
def extract_values(obj, key):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr
    results = extract(obj, arr, key)
    return results

#Getting Current Champions 
ChampionData = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"
ChampionJson = requests.get(ChampionData).json()

champ_names = extract_values(ChampionJson, 'name')
champ_keys = extract_values(ChampionJson, 'key')

champs = dict(zip(champ_keys, champ_names))
print(champs)
 
while True:

    Summoner_Raw = input('Enter Summoner Name: ')
    Summoner = Summoner_Raw.replace(' ', '%20')
    if Summoner_Raw == "quit" or Summoner_Raw == "q":
        print("Quitting...")
        break
    SummonerName = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+ Summoner +'?api_key=' + RIOT_API_KEY

    json_data_summonerID = requests.get(SummonerName).json()
    
    try:
        summonerId = json_data_summonerID['id']
        accountId = json_data_summonerID['accountId']
   
    except: 
        print("No Summoner Found!")
        status = json_data_summonerID['status']['message']
    if status == "OK":
        #print(accountId)
        matchHistory(accountId)
        
        break
    else:
        status = "OK"
        print()