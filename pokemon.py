# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as BS
import webbrowser
import sys

print("Conectando...")
url = "https://www.thewatchcartoononline.tv/anime/pokemon-season-1-indigo-league"
req = requests.get(url)
soup = BS(req.content , "html5lib")
content = soup.find_all(class_="sonra")

def scrape(last_episode):
    last_episode = int(last_episode) + 1
    if (len(str(last_episode)) == 1):
        last_episode = " " + str(last_episode)
    last_episode = last_episode
    print (last_episode)
    global episodes
    episodes = len(content)
    for element in content :
        print (element.text)
        print (element["href"])
        if (last_episode == element.text[-2:]):
            link = element["href"]
            print (element["href"])
            webbrowser.open(link)

            break

def insert() : 
    print("A opção escolhida foi a número 1 - Inserir último episódio assistido.")
    global season
    season = input("Digite o número da temporada : ")
    global last_episode
    last_episode = input("Diga o último episódio assistido : ")
    episode = "episode.txt"
    f = open(episode, "w")
    f.write(last_episode)
    print("Deseje realizar mais alguma coisa ?")
    print("1- Sim")
    print("2- Não")
    option = input()
    if (int(option) == 1):
        main()
    sys.exit()

def next_episode():
    print("A opção escolhida foi a número 1 - Assistir próximo episódio.")
    episode = "episode.txt"
    try :
        f = open(episode, "r")
        global last_episode
        last_episode = f.read()
    except :
        print("Arquivo contendo inexistente")
        f = open(episode, "w")
        f.write("0")
        sys.exit()

    print ("O último episódio assistido foi o episódio " + last_episode)
    scrape((last_episode))
    #sys.exit()

def main():

    print("Digite o que deseja fazer : ")
    print("1- Inserir último episódio assido")
    print("2- Assistir próximo episódio")
    option = 0
    while (option != 1 and option != 2):
        try:
            option = int((input()))
        except:
            print ("Opção invalida")
    
    if (option == 1):
        insert()
    elif (option == 2):
        next_episode()
    else:
        print ("Opção inválida.")

if __name__ == '__main__':
    main()