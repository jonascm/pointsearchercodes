import numpy as np
import random
from random import *
import datetime
import csv
from py2neo import Graph, Path, authenticate
from py2neo import Node
from py2neo import Relationship
import os
import uuid

def datetostr(var):
    styr = str(var.year).zfill(4)
    stmt = str(var.month).zfill(2)
    stdy = str(var.day).zfill(2)
    dateheader = stmt + stdy + styr
    return(dateheader)

def miles7by7(ori, des, depdatemid, retdatemid):
    # here I should do the scraping part... for now I'll return 4 lists of elements: datedep, dateret, miles, dollars
    listorigdt = []
    listretdt = []
    listmiles = []
    listdoll = []
    for rw in range(0,7):
        depdate = depdatemid - datetime.timedelta(days=3) + datetime.timedelta(days=rw)
        for cl in range(0,7):
            retdate = retdatemid - datetime.timedelta(days=3) + datetime.timedelta(days=cl)
            listorigdt.append(datetostr(depdate))
            listretdt.append(datetostr(retdate))
            listmiles.append(str(10000+1000*randint(1, 25)))
            listdoll.append(str(randint(1, 125)))
    return([listorigdt,listretdt,listmiles,listdoll])


def createorupdatedatabase(graph, citini, citifin, depdate, retdate, miles, dollars):
    # already all strings
    # each node is citini + citifin + depdate OR citini + citifin + retdate... see if exist
    qr = 'MATCH (a {name:"' + citini + citifin + depdate + '"}) RETURN a'
    data1 = graph.run(qr)
    orignexist = 0
    for duks in data1:
        orignexist +=1

    if orignexist == 0:
        # origin doesnt exist. Create origin node
        cmdstr = 'CREATE (p:Date { name: "' + citini + citifin + depdate + '" })'
        mknd = graph.run(cmdstr)

    qt = 'MATCH (a {name:"' + citini + citifin + retdate + '"}) RETURN a'
    data2 = graph.run(qr)
    destnexist = 0
    for duks in data1:
        destnexist +=1

    if destnexist == 0:
        # destination doesnt exist. Create origin node
        cmdstr = 'CREATE (p:Date { name: "' + citini + citifin + retdate + '" })'
        mknd = graph.run(cmdstr)

    # now they DO exist: make or update the connection...
    qu = 'MATCH (a {name:"' + citini + citifin + depdate + '"})-[r]-(b {name:"' + citini + citifin + retdate + '"}) DELETE r'
    data3 = graph.run(qu)

    qv = 'MATCH (a {name:"' + citini + citifin + depdate + '"}),(b {name:"' + citini + citifin + retdate + '"}) CREATE (a)-[r:`' + miles + '+$' + dollars +'`]->(b) RETURN r'
    data4 = graph.run(qv)

    print(citini + citifin + " " + depdate + " " + retdate + " for:" + miles + " miles plus $" + dollars)


# mainfunction here

authenticate("localhost:7474", "neo4j", "OnPoint1!")
graph = Graph("http://localhost:7474/db/data/")

cities_usa = ["ATL","JFK","LGA","SFO","LAX","MIA","FLL","MSY","BOS","ORD","HOU","SLC","CLT","SEA","MSP"]
cities_caribbean = ["MEX","CUN","PTY","SJO","NAS","PUJ","MBJ","SJU","SLU","AUA"]
cities_latam = ["EZE","RIO","BOG","CTG","LIM","SCL","UIO","MAO"]
cities_europe = ["BCN","MAD","CDG","HTR","DUS","ATH","FCO","OSL","MOW","DUB","PRG","WAW","BER","AMS","IST"]
cities_africa = ["JNB","LOS","CAI","NBO","CAS"]
cities_asia = ["NRT","JKT","TLV","SYD","SHA","DXB","BOM"]

numofdates = 70
sizeretmat = 7
numofsearches = numofdates/sizeretmat

for citini in cities_usa:
    for citifin in cities_usa:
        currdate = datetime.date.today() + datetime.timedelta(days=3)
        if citini != citifin:
            for ii in range(0,numofsearches):
                iipos = ii * sizeretmat
                for addedval in range(0,sizeretmat):
                    if addedval == 3:
                        datestocallini = currdate
                    if addedval == 4:
                        datestocallfin = currdate
                    currdate += datetime.timedelta(days=1)
        
                for jj in range(ii,numofsearches):
                    jjpos = jj * sizeretmat
                
                    listofthings = miles7by7(citini, citifin, datestocallini,  datestocallfin +  datetime.timedelta(days=jjpos))
                    # create or update database
                    for upd in range(0,len(listofthings[0])):
                        # citini, citifin, depdate, retdate, miles, dollars
                        createorupdatedatabase(graph, citini, citifin, str(listofthings[0][upd]), str(listofthings[1][upd]), str(int(listofthings[2][upd])), str(listofthings[3][upd]))










