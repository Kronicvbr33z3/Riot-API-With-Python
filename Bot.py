import urllib
import requests
"""
Tool that will provide information about a summoner in python
"""

print("League of Legends Tool!")
print("Made by Kronic Vayne, Version: 0.1")

#Getting Summoner Name(Replacing Spaces with %20 for url usage)

Summoner_Raw = input('Enter Summoner Name: ')
Summoner = Summoner_Raw.replace(' ', '%20')

SummonerName = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'+ Summoner +'?api_key=RGAPI-888e39fd-576c-4d22-83dd-2678186ef630'

json_data_summonerID = requests.get(SummonerName).json()
summonerId = json_data_summonerID['id']

print()

choice = input("")