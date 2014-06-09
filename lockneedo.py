import requests
import math
 
STEAM_API_KEY = "27B59C77A29718657FF5F500FBAB966C"
profile = raw_input("Copy The profile's id I.E. numbers after Profile/number")
profile
r = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+ STEAM_API_KEY + "&steamid="+ profile+"&format=json")
 
data = r.json()["response"]["games"]
array = []
for game in data:
	
	array.append(game["playtime_forever"])

total = sum(array)/60
days = total/24


print "This account has played %s hours or %s days" %(total,days)