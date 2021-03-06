#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, webbrowser, sys, season
from bs4 import BeautifulSoup as BS

global episode
global size
size = 0
episode = "episode.txt"

def conect(serie, last_episode):
    size = len(last_episode)
    print (size)
    print("Conectando...")
    url = season.season(serie)
    print(serie)
    print(url)
    req = requests.get(url)
    soup = BS(req.content , "html5lib")
    content = soup.find_all(class_="sonra")
    last_episode = int(last_episode) + 1
    if (len(str(last_episode)) == 1):
        last_episode = " " + str(last_episode)
    last_episode = str(last_episode)
    print (last_episode)
    global episodes
    episodes = len(content)
    for x in range(5):
        for element in content :
            print (element.text[2:])
            print (str(last_episode) + " :")
            if (last_episode == element.text[-size:]):
                link = element["href"]
                print (element["href"])
                webbrowser.open(link)
                break
        last_episode = int(last_episode) + int(1)

def just_watch():
    serie = input("Digite a temporada que deseja assistir : ")
    episode = int(input("Digite o número do episódio que deseja assistir : ")) - 1
    conect(serie, episode)

def last_season():
    f = open(episode, "r")
    a = f.readline().rstrip("\n")
    return (a)

def last_episode():
    f = open(episode, "r")
    a = f.readline()
    b = f.readline()
    size = len(str(b))
    print(size)
    return (b)

def insert() : 
    print("A opção escolhida foi a número 1 - Inserir último episódio assistido.")
    global season
    season = input("Digite o número da temporada : ")
    global last_episode
    last_episode = input("Diga o último episódio assistido : ")
    f = open(episode, "w")
    f.write(season + "\n")
    f.write(last_episode)
    f.close()
    print("Deseje realizar mais alguma coisa ?")
    print("1- Sim")
    print("2- Não")
    option = input()
    if (int(option) == 1):
        main()
    sys.exit()

def check():
    print("Temporada : " + last_season())
    print ("Episódio : " + last_episode())

def next_episode():
    print("A opção escolhida foi a número 3 - Assistir próximo episódio.")
    try :
        last_episode = last_episode()
    except :
        print("Arquivo contendo número do episódio inexistente")
        f = open(episode, "w")
        f.write("0")
        sys.exit()

    print ("O último episódio assistido foi o episódio " + str(last_episode))
    if (last_episode >= len(teste.content)):
        print("Você já assistiu todos os episódios disponíveis")
        sys.exit()

    conect(last_season() , last_episode())

def main():
    last_season()
    last_episode()

    print("Digite o que deseja fazer : ")
    print("1 - Inserir último episódio assido.")
    print("2 - Verificar último episódio assistido.")
    print("3 - Assistir próximo episódio.")
    print("4 - Assistir episódio específico.")
    option = 0
    while (option != 1 and option != 2 and option != 3 and option != 4):
        try:
            option = int(input())
        except:
            print ("Opção invalida")
    
    if (option == 1):
        insert()
    elif (option == 2):
        check()
    elif (option == 3):
        conect(last_season() , last_episode())
        #next_episode()
    elif (option == 4):
        just_watch()
    else:
        print ("Opção inválida.")

if __name__ == '__main__':
    main()
