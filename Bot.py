
import requests
"""
Tool that will provide information about a summoner in python
"""
RIOT_API_KEY = 'RGAPI-f1784676-86a3-4132-9990-c27271266577'
status = "OK"
print("League of Legends Tool!")
print("Made by Kronic Vayne, Version: 0.1")
print("----------------------------------")
#Getting Summoner Name(Replacing Spaces with %20 for url usage)
def analyzeMatch(matchId):
    MatchURL = 'https://na1.api.riotgames.com/lol/match/v3/matches/' + str(matchId) + '?api_key=' + RIOT_API_KEY
    match_json = requests.get(MatchURL).json()
    foundPlayer = False
    
    i = 0
    participantId = 0
    while i >= 10:
      
      tempPlayer = match_json['participantIdentities'][i]['currentAccountId']
      print(tempPlayer)
      i += 1 
      """
      if tempPlayer == Summoner_Raw:
        participantId =  match_json['participantIdentities'][i]['participantId']
        
        foundPlayer = True
      else:
        i += 1
      """
    

    MatchHistory = 'https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/' + str(id) +'/recent?api_key=' + RIOT_API_KEY
    match_history_json = requests.get(MatchHistory).json()
    mMatches = match_history_json['endIndex']
    cMatches = match_history_json['startIndex']
    
    while cMatches <= 5:
        tempChampId = match_history_json['matches'][cMatches]['champion']
        
        tempChampionURL = 'https://na1.api.riotgames.com/lol/static-data/v3/champions/' + str(tempChampId) + '?locale=en_US&api_key=' + RIOT_API_KEY
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
        
    
while True:

    Summoner_Raw = input('Enter Summoner Name: ')
    Summoner = Summoner_Raw.replace(' ', '%20')
    if Summoner_Raw == "quit" or Summoner_Raw == "q":
        print("Quitting...")
        break
    SummonerName = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'+ Summoner +'?api_key=' + RIOT_API_KEY

    json_data_summonerID = requests.get(SummonerName).json()
    
    try:
        summonerId = json_data_summonerID['id']
        accountId = json_data_summonerID['accountId']
   
    except: 
        print("No Summoner Found!")
        status = json_data_summonerID['status']['message']
    if status == "OK":
        matchHistory(accountId)
        break
    else:
        status = "OK"
        print()
