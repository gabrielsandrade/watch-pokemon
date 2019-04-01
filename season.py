import sys

###Variaveis contendo link para cada série###

def season(number):
	#Indigo League
	if (number == "1"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-1-indigo-league"
	#Orange Island League
	if (number == "2"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-2-orange-islands-league"
	#Johto Journeys
	if (number == "3"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-3-the-johto-journeys"
	#Johto League Champions
	if (number == "4"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-4-johto-league-champions"
	#Master Quest
	if (number == "5"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-5-master-quest"
	#Advanced
	if (number == "6"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-6-advanced"
	#Advanced Challenge
	if (number == "7"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-7-advanced-challenge"
	#Advanced Battle	
	if (number == "8"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-8-advanced-battle"
	#Battle Frontier	
	if (number == "9"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-9-battle-frontier"
	#Diamond and Pearl	
	if (number == "10"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-10-diamond-and-pearl"
	#DP Battle Dimension	
	if (number == "11"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-11-dp-battle-dimension"
	#DP Galactic Battles	
	if (number == "12"):
		return "https://www.thewatchcartoononline.tv/anime/pokemon-season-12-dp-galactic-battles"
	#Está faltando mais algumas séries como X/Y/Etc
	else:
		print ("Erro")
		sys.exit()
		return "https://www.google.com.br"